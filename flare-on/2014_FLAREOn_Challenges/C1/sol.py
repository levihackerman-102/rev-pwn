with open("dat_secret", "rb") as fo:
    c = fo.read()
    
print(c)

print("".join([chr((b >> 4 | (b << 4 & 240)) ^ 41) for b in c]))
