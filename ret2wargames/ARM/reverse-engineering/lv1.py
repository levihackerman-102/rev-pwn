import interact
import struct
import re

def p32(n):
    return struct.pack('I', n)

def u32(s):
    return struct.unpack('I', s)[0]

p = interact.Process()

for i in range(100):
    try:
        data = p.readuntil("?").decode()
        print(f"Round {i+1}: {data.strip()}")

        match = re.search(r"What is (-?\d+) ([\+\-\*/]) (-?\d+)", data)
        
        if match:
            a = int(match.group(1))
            op = match.group(2)
            b = int(match.group(3))

            if op == '+': result = a + b
            elif op == '-': result = a - b
            elif op == '*': result = a * b
            elif op == '/': result = a // b
            
            # --- FIXED LOGIC ---
            if result >= 1024:
                print(f"[*] Result is {result}. Sending 1024 to trigger backdoor!")
                p.sendline("1024")
                
                # The program will print "Incorrect", then the flag, and terminate.
                # readall() grabs everything in the buffer until the process closes.
                print(p.readuntil("flag: ").decode())
                print(p.readline().decode())
                break
            else:
                p.sendline(str(result))
                feedback = p.readline().decode()
                print(feedback.strip())
            # ----------------------
            
        else:
            print("Regex failed to match the question format.")
            break

    except EOFError:
        print("\n[!] Connection closed or program finished.")
        break

p.interactive()
