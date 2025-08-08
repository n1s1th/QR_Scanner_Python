import qrcode

# Text to encode
data = "Hello, this is a QR code!"

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
img.save('qrcode.png')
print("QR code generated and saved as qrcode.png")