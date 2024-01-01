def caesar_cipher(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char

    return result

# Contoh penggunaan
plaintext = "helloworld"
shifts = [3, 4, 5]
cipher_texts = []

# Enkripsi
for shift in shifts:
    cipher_text = caesar_cipher(plaintext, shift)
    cipher_texts.append(cipher_text)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext (Shift {shift}): {cipher_text}")
    print()

# Dekripsi
for shift, cipher_text in zip(shifts, cipher_texts):
    decrypted_text = caesar_cipher(cipher_text, -shift)
    print(f"Ciphertext (Shift {shift}): {cipher_text}")
    print(f"Decrypted Text (Shift {shift}): {decrypted_text}")
    print()
