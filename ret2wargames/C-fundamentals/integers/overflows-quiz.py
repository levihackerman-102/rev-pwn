#!/bin/python2

import struct
import re

# --- TOOLS ----

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

num_one = b"4294922645"
num_two = b"2873348155"

num_one = u64(num_one)
num_two = u64(num_two)

answer = num_one - num_two
print(str(answer))

