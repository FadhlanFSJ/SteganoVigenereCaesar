# # Fungsi untuk mengubah pesan menjadi nomor ASCII yang digabung
# def string_to_ascii(message):
#     return int(''.join(str(ord(char)) for char in message))

# # Fungsi untuk memecah nilai menjadi 3 bagian
# def split_value(value):
#     value_str = str(value)
#     return [int(value_str[i:i+3]) for i in range(0, len(value_str), 3)]

# # Fungsi untuk membuat tabel periodik
# def create_periodic_table():
#     periodic_table = [
#         ['H', 'He'],
#         ['Li', 'Be', 'B', 'C', 'N', 'O', 'F'],
#         ['Na','Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
#         ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
#         ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe'],
#         ['Cs', 'Ba', 'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn'],
#         ['Fr', 'Ra', 'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'],
#         ['Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'],
#         ['Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
#     ]
#     return periodic_table

# # Fungsi untuk melakukan enkripsi
# def encrypt(message, a):
#     ascii_value = string_to_ascii(message)
#     splitted_values = split_value(ascii_value)

#     print("Nilai ASCII: ", ascii_value)
#     print("NIlai ASCII setelah displit: ", splitted_values)

#     result = ""
#     for value in splitted_values:
#         if value == 0 or value < 100:
#             cipher_text = value % a
#         else:
#             row = int(str(value)[0])
#             col = (value % a)
#             try:
#                 cipher_text = create_periodic_table()[row-1][col-1]
#             except IndexError:
#                 cipher_text = value % a
#         result += str(cipher_text)

#     return result

# # Contoh penggunaan
# pesan = "INFORMATIKA"
# a = 10  # Misalnya
# print("Pesan Awal : ", pesan)
# cipher = encrypt(pesan, a)
# print("Pesan Enkripsi: ", cipher)
