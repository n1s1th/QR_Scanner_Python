import cv2
from pyzbar.pyzbar import decode

def main():
    # Open the USB camera (usually index 0, sometimes 1 or higher)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    print("Press SPACE to capture an image and scan for QR codes. Press ESC to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Show the live camera feed
        cv2.imshow('USB Camera - QR Scanner', frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC key to exit
            break
        elif key == 32:  # SPACE to capture and scan
            # Decode QR codes in the captured frame
            decoded_objects = decode(frame)
            if decoded_objects:
                for obj in decoded_objects:
                    print("Type:", obj.type)
                    print("Data:", obj.data.decode("utf-8"))
            else:
                print("No QR code detected.")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()