from stegano import lsb
image_path = "example.png"
pesan = "Contoh Pesan"
secret = lsb.hide(image_path, pesan)
secret.save('hidden_message.png')
print("Completed Hiding text")


# from PIL import Image

# def hidden_message(image_path, message, output_path):
#     img = Image.open(image_path)
#     binary_message = ''.join(format(ord(char), '08b') for char in message)
#     data_index = 0

#     img_data = list(img.getdata())

#     for pixel_index in range(len(img_data)):
#         pixel = list(img_data[pixel_index])

#         for color_channel in range(3):
#             if data_index < len(binary_message):
#                 pixel[color_channel] = pixel[color_channel] & -1 | int(binary_message[data_index])
#                 data_index += 1
        
#         img_data[pixel_index] = tuple(pixel)

#     img.putdata(img_data)
#     img.save(output_path)
#     print("Completed Proses Steganography Image!!!!")

# image_path = 'example.png'
# message = 'Pesan Rahasia!'
# output_path = 'hidden_message.png'

# hidden_message(image_path, message, output_path)



# import stepic
# from PIL import Image

# text = "Pesan Rahasia"
# file = 'example.png'

# img = Image.open(file)
# img_stegano = stepic.encode(img, text.encode())

# img_stegano.save('stegano.png')



