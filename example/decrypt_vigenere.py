def vigenere_decrypt(cipher_text, keys):
    decrypted_text = ""
    key_length = len(keys)
    
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        key = keys[i % key_length]
        
        if char.isalpha():
            # Shift character based on the key for decryption
            shift = ord(key) - ord('A') if key.isupper() else ord(key) - ord('a')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            # Non-alphabetic characters are not decrypted
            decrypted_text += char
    
    return decrypted_text

def decrypt_multiple_keys(cipher_text, keys):
    decrypted_text = cipher_text
    for key in keys[::-1]:  # Reverse the order of keys for decryption
        decrypted_text = vigenere_decrypt(decrypted_text, key)
    return decrypted_text

# Contoh penggunaan untuk decrypt:
cipher_text = "LPWVZIOVDDR MHUDRYQO"
keys = ["REKAYASA", "PERANGKAT", "LUNAK"]

decrypted_text = decrypt_multiple_keys(cipher_text, keys)
print("Cipher Text:", cipher_text)
print("Decrypted Text:", decrypted_text)