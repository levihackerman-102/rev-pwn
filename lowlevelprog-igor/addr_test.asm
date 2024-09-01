section .data
    test: dq -1                  ; Define a 64-bit variable initialized to -1
    buffer db '0000000000000000', 0 ; Buffer for converting test to a string
    newline db 10, 0            ; Newline character for formatting

section .bss
    numstr resb 21              ; Buffer to hold the string representation of the number (including null terminator)

section .text
    global _start

_start:
    ; Move 1 into the first byte of test
    mov byte [test], 1          ; Set the lowest byte of test to 1
    call print_test             ; Print the value of test

    ; Move 1 into the first word of test
    mov word [test], 1          ; Set the lowest word of test to 1
    call print_test             ; Print the value of test

    ; Move 1 into the first dword of test
    mov dword [test], 1         ; Set the lowest dword of test to 1
    call print_test             ; Print the value of test

    ; Move 1 into the entire qword of test
    mov qword [test], 1         ; Set the entire qword of test to 1
    call print_test             ; Print the value of test

    ; Exit the program
    mov eax, 1                  ; syscall number for sys_exit
    xor ebx, ebx                ; exit code 0
    int 0x80                    ; call kernel

; Function to print the value of test
print_test:
    mov rax, [test]             ; Load the value of test into rax
    mov rdi, numstr             ; Point rdi to the numstr buffer
    call int_to_ascii           ; Convert the integer to an ASCII string

    ; Write the result to stdout
    mov eax, 4                  ; syscall number for sys_write
    mov ebx, 1                  ; file descriptor 1 is stdout
    mov ecx, numstr             ; pointer to the string
    mov edx, 21                 ; length of the string
    int 0x80                    ; call kernel

    ; Print a newline
    mov eax, 4                  ; syscall number for sys_write
    mov ebx, 1                  ; file descriptor 1 is stdout
    mov ecx, newline            ; pointer to the newline character
    mov edx, 1                  ; length of the string
    int 0x80                    ; call kernel

    ret

; Function to convert an integer to a null-terminated ASCII string
; Input: rax - the integer to convert
;        rdi - pointer to the buffer to store the ASCII string
int_to_ascii:
    mov rcx, 10                 ; Divisor for base 10
    mov rbx, rdi                ; Store the starting address of the buffer

int_to_ascii_loop:
    xor rdx, rdx                ; Clear rdx before dividing
    div rcx                     ; Divide rax by 10, quotient in rax, remainder in rdx
    add dl, '0'                 ; Convert remainder to ASCII
    dec rdi                     ; Move to the next position in the buffer
    mov [rdi], dl               ; Store the ASCII character
    test rax, rax               ; Check if quotient is zero
    jnz int_to_ascii_loop       ; If not, continue looping

    mov rax, rbx                ; Restore original buffer address
    sub rax, rdi                ; Calculate the length of the string
    add rdi, rax                ; Move the pointer to the end of the string

    mov byte [rdi], 0           ; Null-terminate the string
    ret
