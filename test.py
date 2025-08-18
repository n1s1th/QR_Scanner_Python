import cv2
from pyzbar.pyzbar import decode

def scan_qr_from_custom_crop(crop_x, crop_y, crop_width, crop_height, camera_index=2):
    """
    Captures an image from the webcam, crops the region defined by (crop_x, crop_y, crop_width, crop_height),
    scans for a QR code in that region, and returns the decoded data if found.

    Args:
        crop_x (int): X coordinate of the top-left corner of the crop area.
        crop_y (int): Y coordinate of the top-left corner of the crop area.
        crop_width (int): Width of the crop area.
        crop_height (int): Height of the crop area.
        camera_index (int): Index of the camera (default: 0).

    Returns:
        str or None: Decoded QR code data, or None if not found.
    """
    cap = cv2.VideoCapture(camera_index)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Failed to capture image.")
        return None

    h, w = frame.shape[:2]
    # Ensure crop area is within bounds
    crop_x = max(0, min(crop_x, w - crop_width))
    crop_y = max(0, min(crop_y, h - crop_height))
    crop_width = min(crop_width, w - crop_x)
    crop_height = min(crop_height, h - crop_y)

    cropped = frame[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]
    decoded_objects = decode(cropped)
    for obj in decoded_objects:
        return obj.data.decode("utf-8")  # Return the data of the first QR code found

    return None  # No QR code found

# Example usage
if __name__ == "__main__":
    # Example crop coordinates: top-left corner (120, 200), size 250x250
    data = scan_qr_from_custom_crop(88, 232, 250, 250)
    print("QR code data:" if data else "No QR code found.", data)
#crop_x=88, crop_y=232, crop_width=146, crop_height=141