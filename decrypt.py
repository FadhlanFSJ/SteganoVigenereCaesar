from stegano import lsb
import sys

def getting_encrypt_text(image_path):
    try:
        text = lsb.reveal(image_path)
        print("Completed Reveal the Text!")
        return text
    except Exception as e:
        print(f"Error while getting text from {image_path} : {e}")
        sys.exit(0)

def element_symbols_to_text(element_symbols):
    # Kamus data untuk mengaitkan singkatan unsur dengan nomor atom
    element_data = {
        'H': '1', 'He': '2', 'Li': '3', 'Be': '4', 'B': '5',
        'C': '6', 'N': '7', 'O': '8', 'F': '9', 'Ne': '10',
        'Na': '11', 'Mg': '12', 'Al': '13', 'Si': '14', 'P': '15',
        'S': '16', 'Cl': '17', 'Ar': '18', 'K': '19', 'Ca': '20',
        'Sc': '21', 'Ti': '22', 'V': '23', 'Cr': '24', 'Mn': '25',
        'Fe': '26', 'Ni': '27', 'Co': '28', 'Cu': '29', 'Zn': '30',
        'Ga': '31', 'Ge': '32', 'As': '33', 'Se': '34', 'Br': '35',
        'Kr': '36', 'Rb': '37', 'Sr': '38', 'Y': '39', 'Zr': '40',
        'Nb': '41', 'Mo': '42', 'Tc': '43', 'Ru': '44', 'Rh': '45',
        'Pd': '46', 'Ag': '47', 'Cd': '48', 'In': '49', 'Sn': '50',
        'Sb': '51', 'Te': '52', 'I': '53', 'Xe': '54', 'Cs': '55',
        'Ba': '56', 'La': '57', 'Ce': '58', 'Pr': '59', 'Nd': '60',
        'Pm': '61', 'Sm': '62', 'Eu': '63', 'Gd': '64', 'Tb': '65',
        'Dy': '66', 'Ho': '67', 'Er': '68', 'Tm': '69', 'Yb': '70',
        'Lu': '71', 'Hf': '72', 'Ta': '73', 'W': '74', 'Re': '75',
        'Os': '76', 'Ir': '77', 'Pt': '78', 'Au': '79', 'Hg': '80',
        'Tl': '81', 'Pb': '82', 'Bi': '83', 'Po': '84', 'At': '85',
        'Rn': '86', 'Fr': '87', 'Ra': '88', 'Ac': '89', 'Th': '90',
        'Pa': '91', 'U': '92', 'Np': '93', 'Pu': '94', 'Am': '95',
        'Cm': '96', 'Bk': '97', 'Cf': '98', 'Es': '99', 'Fm': '100',
        'Md': '101', 'No': '102', 'Lr': '103', 'Rf': '104', 'Db': '105',
        'Sg': '106', 'Bh': '107', 'Hs': '108', 'Mt': '109', 'Ds': '110',
        'Rg': '111', 'Cn': '112', 'Nh': '113', 'Fl': '114', 'Mc': '115',
        'Lv': '116', 'Ts': '117', 'Og': '118',
        #! Tambahan data yang tidak ada pada Tabel Periodik, agar data tetap ter dekripsi!
        'Xy': '119', 'Bc': '120', 'Zf': '121', 'We': '122'
    }

    # Memecah simbol unsur menjadi pasangan dua huruf
    symbol_pairs = []
    i = 0
    while i < len(element_symbols):
        pair = element_symbols[i]
        if i + 1 < len(element_symbols) and element_symbols[i + 1].islower():
            pair += element_symbols[i + 1]
            i += 1
        symbol_pairs.append(pair)
        i += 1

    # print("Symbol Pairs : ", symbol_pairs)

    # Mengekstrak nomor atom dari kamus data
    atom_numbers = [element_data.get(pair, '??') for pair in symbol_pairs]
    # print("Atom Number : ", atom_numbers)

    # Menggabungkan pasangan dua digit menjadi nilai ASCII
    ascii_values = [int(number) if number.isdigit() else ord('?') for number in atom_numbers]

    # Mengonversi nilai ASCII ke karakter
    decrypted_text = ''.join(chr(value) for value in ascii_values)

    return decrypted_text

def decrypt_custom_caesar_cipher(ciphertext, shift_keys):
    decrypted_text = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = shift_keys[key_index]
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(shift_keys)
        else:
            decrypted_text += char

    return decrypted_text

def decrypt_multiple_keys(cipher_text, keys):
    decrypted_text = cipher_text
    for key in keys[::-1]:  # Reverse the order of keys for decryption
        decrypted_text = vigenere_decrypt(decrypted_text, key)
    return decrypted_text

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



image_path = 'hidden_message.png'
shift_keys = [3, 4, 5]
keys = input("Masukkan Key Vigenere sebanyak 3 (Pisahkan dengan Spasi): ").split()
print("Key Vigenere : ", keys)
encrypted_text = getting_encrypt_text(image_path)
print("Encrypted Text: ",encrypted_text)
caesar_cipher_text = element_symbols_to_text(encrypted_text)
print("Caesar Cipher Text : ", caesar_cipher_text)
vigenere_cipher_text = decrypt_custom_caesar_cipher(caesar_cipher_text, shift_keys)
print("Vigenere Cipher Text : ", vigenere_cipher_text)
plain_text = decrypt_multiple_keys(vigenere_cipher_text, keys)
print("Pesan : ", plain_text)
