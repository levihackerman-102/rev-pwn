def predict_otp(seed):
    """
    Predicts the 8-character OTP based on a given seed value.
    This replicates the generate_OTP function from the provided assembly.
    
    Args:
        seed: An integer seed value (from current_session+0x30)
        
    Returns:
        An 8-character string representing the predicted OTP
    """
    otp = ""
    
    for i in range(8):  # Loop runs 8 times (index 0-7)
        # Replicate the assembly calculations
        eax = i * 2  # add eax, eax
        edx = 0x3059b9c1 >> eax  # mov edx, 0x3059b9c1; sar edx, cl
        eax = edx & 0xFF  # movzx eax, al
        ecx = eax ^ seed  # xor eax, dword [rbp-0x8]
        
        # This block replicates the division by 9 using the magic number multiplication
        # It's equivalent to ecx % 9
        # mov edx, 0x38e38e39; imul edx; sar edx, 0x1; sub edx, eax>>31
        edx = (ecx * 0x38e38e39) >> 32  # imul result goes in edx
        edx = edx >> 1  # sar edx, 0x1
        eax_sign = 1 if ecx < 0 else 0  # mov eax, ecx; sar eax, 0x1f
        edx = edx - eax_sign  # sub edx, eax
        
        # Calculate the remainder
        eax = edx * 9  # multiply by 9 (8+1)
        ecx = ecx - eax  # This gives us ecx % 9
        
        # Add 0x31 (ASCII '1') to make it a printable character
        char_code = ecx + 0x31
        otp += chr(char_code)
    
    return otp

seed = 1740938375
print(predict_otp(seed))
