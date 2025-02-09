values = [
    0x75, 0x3a, 0xc0, 0xc8, 0x33, 0xcf, 0xcc, 0x2e, 
    0xcc, 0xc7, 0x17, 0xec, 0xb0, 0x37, 0xeb, 0x9b, 0x70,
    0xe6, 0x8c, 0x63, 0xa7
]

real_values = [x ^ (i * 0x54) for i, x in enumerate(values)]
password_encrypted = "".join([chr(x) for x in real_values])
print(password_encrypted)

# values_pass = [0x75, 0x6e, 0x68, 0x34, 0x63, 0x6b, 0x34, 0x62, 0x6c, 0x33, 0x5f, 0x70, 0x40, 0x73, 0x73, 0x77, 0x30, 0x72, 0x64, 0x5f, 0x37]
# password = "".join([chr(x) for x in values_pass])

# print(password)
    
