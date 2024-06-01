import string

def custom_cipher(text):
    # Remove whitespace and punctuation, convert to lower case
    text = text.translate(str.maketrans('', '', string.whitespace + string.punctuation))
    text = text.lower()

    # Perform shift of +4 (mod 26) and convert to upper case
    shifted = []
    for c in text:
        shifted.append(chr(((ord(c) - ord('a') + 4) % 26) + ord('A')))

    # Create output array of ordinal values at even and odd positions
    even = [ord(shifted[i]) for i in range(0, len(shifted), 2)]
    odd = [ord(shifted[i]) for i in range(1, len(shifted), 2)]
    output = even + odd

    # Print output array in groups of five characters
    for i, val in enumerate(output):
        if i > 0 and i % 5 == 0:
            print()
        print(f"0x{val:02X}", end=" ")

# Example usage
custom_cipher("Hello, World!")
