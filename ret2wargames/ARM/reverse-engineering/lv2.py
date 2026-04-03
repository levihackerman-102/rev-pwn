import interact

p = interact.Process()

def solve_lock(key):
    # Extract the 4 bytes from the 32-bit key
    b0 = key & 0xFF
    b1 = (key >> 8) & 0xFF
    b2 = (key >> 16) & 0xFF
    b3 = (key >> 24) & 0xFF
    
    # Calculate base solutions
    t0 = b0
    t1 = (((b1 * 7) ^ 0x12) + 1) & 0xFF
    t2 = ((b2 ^ 0x55) + 0x0A) & 0xFF
    
    t3 = 0
    for i in range(1, 4):
        t3 = (t3 + (b3 ^ (i + 0x27))) & 0xFF
        
    # Apply adjust_sol (add the index 'i' to each target)
    ans0 = (t0 + 0) & 0xFF
    ans1 = (t1 + 1) & 0xFF
    ans2 = (t2 + 2) & 0xFF
    ans3 = (t3 + 3) & 0xFF
    
    return [ans0, ans1, ans2, ans3]

# Read output until the serial number is printed
output = p.readuntil("number on the bottom: ").decode()
key_line = p.readline().decode().strip()
key = int(key_line)

print(f"[*] Extracted Serial Number: {key}")

# Calculate the adjusted targets
targets = solve_lock(key)
print(f"[*] Calculated Adjusted Targets: {[hex(t) for t in targets]}")

# Loop through the 4 stages and send the answers in hexadecimal
for i, ans in enumerate(targets):
    p.readuntil("enter number of clicks:")
    
    hex_ans = hex(ans)[2:]  # Strip the '0x' prefix
    print(f"[*] Stage {i+1}: Sending {hex_ans}")
    
    p.sendline(hex_ans)

p.interactive()
