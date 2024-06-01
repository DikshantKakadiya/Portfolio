import string

def encrypt(plaintext):
    # Remove whitespace and punctuation
    plaintext = ''.join(c for c in plaintext if c not in string.whitespace and c not in string.punctuation)

    # Convert to lowercase
    plaintext = plaintext.lower()

    # Perform shift
    ciphertext = ''
    for c in plaintext:
        ciphertext += chr(((ord(c) - ord('a') + 4) % 26) + ord('A'))

    # Create output array
    output = []
    for i in range(0, len(ciphertext), 2):
        output.append(ord(ciphertext[i]))
    for i in range(1, len(ciphertext), 2):
        output.append(ord(ciphertext[i]))

    # Print in groups of 5
    for i in range(0, len(output), 5):
        print(' '.join([hex(x) for x in output[i:i+5]]))

def decrypt(ciphertext):
    # Convert back to ordinal values
    ciphertext = [int(x, 16) for x in ciphertext.split()]

    # Convert back to characters
    plaintext = ''
    for i in range(0, len(ciphertext)//2):
        plaintext += chr(((ciphertext[i] - ord('A') - 4) % 26) + ord('a'))
        plaintext += chr(((ciphertext[i+len(ciphertext)//2] - ord('A') - 4) % 26) + ord('a'))

    print(plaintext)
plaintext = "Hello, World!"
print("Encrypting:", plaintext)
encrypt(plaintext)

ciphertext = "0x4C 0x50 0x53 0x53 0x50\n0x49 0x50 0x41 0x56 0x48"
print("\nDecrypting:", ciphertext)
decrypt(ciphertext)
