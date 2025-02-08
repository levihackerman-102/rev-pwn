req = "ycbwkgyucbgfajd"
xorkey = 0x21
key = ''.join([chr(ord(i)^xorkey) for i in req])
print(key)
