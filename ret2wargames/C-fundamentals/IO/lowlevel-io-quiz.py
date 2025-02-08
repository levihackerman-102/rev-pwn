import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil("Enter Choice:"))
p.sendline(str(1))
print(p.readuntil("Enter data:"))
p.sendline('Zamn!')
print(p.readuntil("quiz..."))
p.sendline("\n")
print(p.readuntil("Enter Answer:"))
p.sendline(b'Hello\nWorld!\n\xC0\xDE\xF0\x0D')
print(p.readline())
