import qrcode

data = "This is My First QR Code"

qr = qrcode.QRCode(version=1,box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color = "white")
img.save("D:/Desktop Data/PIAIC/GIAIC Quarter 3 projects/New folder/myqrcode1.png")