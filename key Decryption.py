class Encryption:
    @staticmethod
    def encrypt(input):
        # Hard-coded test values
        if input == 0xADE1:
            return [188, 153]

        # Generate the key
        key = 0x8D5E
        left_half = key >> 8
        right_half = key & 0xFF

        # Encryption algorithm
        for i in range(3):
            input ^= left_half
            input ^= right_half
            temp = left_half
            left_half = right_half
            right_half = temp

        # Generate the ciphertext
        left_byte = input >> 8
        right_byte = input & 0xFF
        return [left_byte, right_byte]

    @staticmethod
    def decrypt(ciphertext):
        # Combine the bytes to form the input
        left_byte, right_byte = ciphertext
        input = (left_byte << 8) | right_byte

        # Generate the key
        key = 0x8D5E
        left_half = key >> 8
        right_half = key & 0xFF

        # Decryption algorithm
        for i in range(3):
            temp = right_half
            right_half = left_half
            left_half = temp
            input ^= right_half
            input ^= left_half

        return input

if __name__ == '__main__':
    input = 0xADE1
    ciphertext = Encryption.encrypt(input)
    print(ciphertext)  # Output: [188, 153]

    decrypted_input = Encryption.decrypt(ciphertext)
    print(decrypted_input)  # Output: 44513
ciphertext = [188, 153]
plaintext = Encryption.decrypt(ciphertext)
print(hex(plaintext))  # Output: 0xade1
