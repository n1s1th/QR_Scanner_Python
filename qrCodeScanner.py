import cv2
from pyzbar.pyzbar import decode

# Load image containing QR code
img = cv2.imread('Sample_QR_Codes/qrcode.png')

# Decode QR codes in the image
decoded_objects = decode(img)

for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode("utf-8"))

#If you want to scan from webcam:
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     decoded_objects = decode(frame)
#     for obj in decoded_objects:
#         print("Data:", obj.data.decode("utf-8"))
#     cv2.imshow('QR Scanner', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()