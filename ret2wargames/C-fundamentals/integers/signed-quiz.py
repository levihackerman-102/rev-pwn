#!/bin/python2
# ============================================================================== #
# integers-signed.py --------------------------------------------------------- # 
# ============================================================================== #
# Python 2.x.x ----------------------------------------------------------------- #
# Author: Frederick Pellerin --------------------------------------------------- #
# GitHub: https://github.com/TheRealFREDP3D ------------------------------------ #
# X:      https://twitter.com/TheRealFredP3D ----------------------------------- #
# ============================================================================== #
# ---- C Fundamentals ----
# ---- Integers ----
# ---- Signed ----
# ---- Solution ----

import interact
import struct
import re

# --- TOOLS ----

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

#  ---- SOLUTION ----

p = interact.Process()
p.readuntil('Choice:')
p.sendline('2')


p.readuntil('quiz...')
p.sendline('\n')

# ---- PROGRAM OUTPUT ----
#
# ---- SKILL QUIZ ----
# What will the following C code print:
#    int foo = 0xEBC9C183;
#    printf("%d", foo);
# Enter Answer:

# 1

p.readuntil('foo = ')
answer = p.readuntil(';\n')
answer = answer.strip(b';\n')

# print(answer)  # This will print the hexadecimal string

# Remove ANSI color codes
answer_clean = re.sub(b'\x1b\[[0-9;]*m', b'', answer)
# print(answer_clean)  # This will print the clean hexadecimal string

# Convert hexadecimal string to integer
answer_int = int(answer_clean, 16)
# print(answer_int)  # This will print the integer value
p.readuntil('Answer:')
p.sendline(str(answer_int))

# 2

p.readuntil('foo = ')
answer = p.readuntil(';\n')
answer = answer.strip(b';\n')

# print(answer)  # This will print the hexadecimal string

# Remove ANSI color codes
answer_clean = re.sub(b'\x1b\[[0-9;]*m', b'', answer)
# print(answer_clean)  # This will print the clean hexadecimal string

# Convert hexadecimal string to integer
answer_int = int(answer_clean, 16)
# print(answer_int)  # This will print the integer value
p.readuntil('Answer:')
p.sendline(str(answer_int))

# --- 

p.interactive()
