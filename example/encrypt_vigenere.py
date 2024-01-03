def vigenere_encrypt(plain_text, keys):
    cipher_text = ""
    key_length = len(keys)
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        key = keys[i % key_length]
        
        if char.isalpha():
            # Shift character based on the key
            shift = ord(key) - ord('A') if key.isupper() else ord(key) - ord('a')
            if char.isupper():
                cipher_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                cipher_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            # Non-alphabetic characters are not encrypted
            cipher_text += char
    
    return cipher_text

def encrypt_multiple_keys(plain_text, keys):
    cipher_text = plain_text
    for key in keys:
        cipher_text = vigenere_encrypt(cipher_text, key)
    return cipher_text

# Contoh penggunaan:
pesan = "UNIVERSITAS BUMIGORA"
keys = ["REKAYASA", "PERANGKAT", "LUNAK"]

cipher_text = encrypt_multiple_keys(pesan, keys)
print("Pesan Asli:", pesan)
print("Cipher Text:", cipher_text)
