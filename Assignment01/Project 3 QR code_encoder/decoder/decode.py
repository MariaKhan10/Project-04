from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("D:/Desktop Data/PIAIC/GIAIC Quarter 3 projects/New folder/myqrcode.png")

result = decode(img)

print(result)