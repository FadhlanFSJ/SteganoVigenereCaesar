from stegano import lsb

def encrypt_multiple_keys(plain_text, keys):
    cipher_text = plain_text
    for key in keys:
        cipher_text = vigenere_encrypt(cipher_text, key)
    return cipher_text

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


def encrypt_custom_caesar_cipher(text, shift_keys):
    encrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = shift_keys[key_index]
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(shift_keys)
        else:
            encrypted_text += char

    return encrypted_text

def text_to_element_symbols(text):
    # Kamus data untuk mengaitkan nomor atom dengan singkatan unsur
    element_data = {
        "1": 'H', "2": 'He', "3": 'Li', "4": 'Be', "5": 'B',
        "6": 'C', "7": 'N', "8": 'O', "9": 'F', "10": 'Ne',
        "11": 'Na', "12": 'Mg', "13": 'Al', "14": 'Si', "15": 'P',
        "16": 'S', "17": 'Cl', "18": 'Ar', "19": 'K', "20": 'Ca',
        "21": 'Sc', "22": 'Ti', "23": 'V', "24": 'Cr', "25": 'Mn',
        "26": 'Fe', "27": 'Ni', "28": 'Co', "29": 'Cu', "30": 'Zn',
        "31": 'Ga', "32": 'Ge', "33": 'As', "34": 'Se', "35": 'Br',
        "36": 'Kr', "37": 'Rb', "38": 'Sr', "39": 'Y', "40": 'Zr',
        "41": 'Nb', "42": 'Mo', "43": 'Tc', "44": 'Ru', "45": 'Rh',
        "46": 'Pd', "47": 'Ag', "48": 'Cd', "49": 'In', "50": 'Sn',
        "51": 'Sb', "52": 'Te', "53": 'I', "54": 'Xe', "55": 'Cs',
        "56": 'Ba', "57": 'La', "58": 'Ce', "59": 'Pr', "60": 'Nd',
        "61": 'Pm', "62": 'Sm', "63": 'Eu', "64": 'Gd', "65": 'Tb',
        "66": 'Dy', "67": 'Ho', "68": 'Er', "69": 'Tm', "70": 'Yb',
        "71": 'Lu', "72": 'Hf', "73": 'Ta', "74": 'W', "75": 'Re',
        "76": 'Os', "77": 'Ir', "78": 'Pt', "79": 'Au', "80": 'Hg',
        "81": 'Tl', "82": 'Pb', "83": 'Bi', "84": 'Po', "85": 'At',
        "86": 'Rn', "87": 'Fr', "88": 'Ra', "89": 'Ac', "90": 'Th',
        "91": 'Pa', "92": 'U', "93": 'Np', "94": 'Pu', "95": 'Am',
        "96": 'Cm', "97": 'Bk', "98": 'Cf', "99": 'Es', "100": 'Fm',
        "101": 'Md', "102": 'No', "103": 'Lr', "104": 'Rf', "105": 'Db',
        "106": 'Sg', "107": 'Bh', "108": 'Hs', "109": 'Mt', "110": 'Ds',
        "111": 'Rg', "112": 'Cn', "113": 'Nh', "114": 'Fl', "115": 'Mc',
        "116": 'Lv', "117": 'Ts', "118": 'Og', 
        #! Tambahan data yang tidak ada pada Tabel Periodik, agar data tetap ter enkripsi!
        "119": 'Xy', "120" : 'Bc', "121": 'Zf', '122': 'We'
    }

    # Mengubah teks menjadi daftar ASCII
    ascii_values = [ord(char) for char in text]
    # print("ASCII Value : ", ascii_values)

    # Membagi daftar ASCII menjadi pasangan dua digit
    digit_pairs = ['{:02d}'.format(value) for value in ascii_values]
    # print("Digit : ", digit_pairs)

    # Mengekstrak unsur dari kamus data
    element_symbols = [element_data.get(pair, '??') for pair in digit_pairs]

    return ''.join(element_symbols)

def insert_text_to_image(text, image_path):
    secret = lsb.hide(image_path, text)
    secret.save('hidden_message.png')
    print("Completed Hiding text")

# Contoh penggunaan:
pesan = input("Masukkan pesan yang ingin di enkripsi: ")
keys = input("Masukkan Key Vigenere sebanyak 3 (Pisahkan dengan Spasi): ").split() # keys = ["Informatika", "Angkatan", "Pertama"]
print("Keys Vigenere :", keys)
shift_keys = [3, 4, 5]
image_path = 'example.png'
print("Pesan Awal : ", pesan)
cipher_text_vigenere = encrypt_multiple_keys(pesan, keys)
print("Cipher Text Vigenere: ", cipher_text_vigenere)
cipher_text_caesar = encrypt_custom_caesar_cipher(cipher_text_vigenere, shift_keys)
print("Cipher Text Caesar : ", cipher_text_caesar)
cipher_text_symbol = text_to_element_symbols(cipher_text_caesar)
print("Cipher Text Symbol : ", cipher_text_symbol)
insert_text_to_image(cipher_text_symbol, image_path)

