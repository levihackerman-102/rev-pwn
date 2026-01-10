import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

# wdb> x/6bx 0x6020b0
# 0x6020b0: 0xd8    0x32    0x5c    0xef    0x05    0x9a
SECRET_ARRAY = [0xd8, 0x32, 0x5c, 0xef, 0x05, 0x9a]

def solve_challenge(challenge_str):
    parts = challenge_str.strip().split('-')
    
    g1 = [ord(c) for c in parts[0]]
    g2 = [ord(c) for c in parts[1]]
    g3 = [ord(c) for c in parts[2]]
    g4 = [ord(c) for c in parts[3]]
    g5 = [ord(c) for c in parts[4]]

    checksum = 0
    for val in g3:
        checksum = (checksum << 5) ^ val
        checksum &= 0xFFFFFFFF
    token1 = str(checksum)

    token2 = ""
    for i in range(6):
        temp = (g1[i] ^ g2[i] ^ g4[i])
        temp = (temp + 1) & 0xFF
        final = temp ^ g3[i]
        
        token2 += "%02X" % final

    token3 = ""
    for i in range(6):
        val = (g5[i] * SECRET_ARRAY[i]) % 26
        token3 += chr(val + 0x41)

    # wdb> x/s 0x401118
    # 0x401118: ":"
    return token1 + ':' + token2 + ':' + token3

p = interact.Process()
p.readline()
p.readline()
p.readline()

for i in range(200):
    data = p.readline()
    print(data)
    chall = data.strip().split(' ')[-1]
    print("chall: {}".format(chall))
    p.readuntil('RESPONSE:')
    resp = solve_challenge(chall)
    print("resp: {}".format(resp))
    p.sendline(resp)

p.interactive()
