from stegano import lsb

file = 'hidden_message.png'
secret_data = lsb.reveal(file)
print("Pesan : ",secret_data)


# from PIL import Image

# def extract_message(image_path):
#     img = Image.open(image_path)
#     binary_message = ""
#     img_data = list(img.getdata())

#     for pixel_index in range(len(img_data)):
#         pixel = img_data[pixel_index]

#         for color_channel in range(3):
#             binary_message += str(pixel[color_channel] & 1)

#     message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
#     return message

# image_path = 'hidden_message.png'
# extracted_message = extract_message(image_path)
# print(f'Message : {extracted_message}')

# import stepic
# from PIL import Image

# file = 'stegano.png'

# img = Image.open(file)
# decoded = stepic.decode(img)
# print("Data : " + str(decoded))

