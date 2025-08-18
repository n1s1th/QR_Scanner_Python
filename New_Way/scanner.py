import cv2
import json
import time
from pyzbar.pyzbar import decode

# Hardcoded JSON path
JSON_PATH = "crop_box.json"

def load_crop_box(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
        return data["x"], data["y"], data["width"], data["height"]

def main():
    # Load box coordinates from json
    crop_x, crop_y, crop_width, crop_height = load_crop_box(JSON_PATH)
    camera_index = 2

    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Failed to open camera at index {camera_index}")
        return

    start_time = time.time()
    qr_data = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read from camera.")
            break

        # Draw the virtual box
        preview = frame.copy()
        cv2.rectangle(
            preview,
            (crop_x, crop_y),
            (crop_x + crop_width, crop_y + crop_height),
            (0, 255, 0),
            2,
        )
        cv2.imshow("Live Camera (Box Area)", preview)

        # Crop area for QR detection
        cropped = frame[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]
        decoded_objects = decode(cropped)
        if decoded_objects:
            qr_data = decoded_objects[0].data.decode("utf-8")
            print("QR Code detected:", qr_data)
            break

        # Terminate after 5 seconds
        if time.time() - start_time > 5:
            print("No QR code detected in 5 seconds.")
            break

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("User quit program.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()