import qrcode

# Text to encode

data = "B2"


# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

# Create and save image
img = qr.make_image(fill='black', back_color='white')

img.save('qrcodeB2.png')

print("QR code generated and saved as qrcode.png")