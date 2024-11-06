def caesar_cipher(text, shift=5):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for char in text:
        if char.isalpha():
            char = char.lower()
            index = alphabet.index(char)
            shifted_index = (index + shift) % 26
            shifted_char = alphabet[shifted_index]
            result.append(shifted_char)
        else:
            result.append(char)

    return ''.join(result)

text = input("Enter text to encrypt: ").lower()
shift = 5 

encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted text: {encrypted_text}")
