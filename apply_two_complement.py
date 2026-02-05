def decimal_to_binary(number):
    binary = bin(number)
    binary = binary[2:]      # Remove the '0b' prefix
    binary = binary.zfill(8) # Pad to 8 bits
    return binary


def apply_two_complement(binary):
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
    inverted_decimal = int(inverted, base=2) + 1
    result_binary = decimal_to_binary(inverted_decimal)
    return result_binary  # Negative binary using two's complement


number = input("Enter a decimal number: ")
number = int(number)

binary = decimal_to_binary(number)
print("Binary is:", binary)

result = apply_two_complement(binary)
print(f"Binary representation of -{number} is: {result}")
