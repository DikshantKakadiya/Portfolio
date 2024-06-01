import random

import string

def RC4(data, key):
    S = list(range(256))
    j = 0
    out = []

    # Key Scheduling Algorithm Phase
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm Phase
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        #swaping 
        S[i], S[j] = S[j], S[i] 
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return ''.join(out)

# Encryption
plaintext = input("enter the text that need to be encryprted by RC4 :")
key_length = len(plaintext)

# Generating a randowm key of lenght of plantext
key = random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=key_length))
ciphertext = RC4(plaintext, key)
print("Encrypted text:", ciphertext)

# Decryption
decrypted_text = RC4(ciphertext, key)
print("Decrypted text:", decrypted_text)