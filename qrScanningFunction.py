import cv2
from pyzbar.pyzbar import decode

def crop_and_scan_qr(crop_coords, camera_index=0):
    """
    Captures a frame from the webcam, crops the given area, scans for QR code, and returns the QR code data.

    Args:
        crop_coords (tuple): (startx, starty, endx, endy) coordinates for cropping the frame.
        camera_index (int): Index of the camera (default 0).

    Returns:
        str or None: Decoded QR code data if found, else None.
    """
    cap = cv2.VideoCapture(camera_index)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return None

    startx, starty, endx, endy = crop_coords
    cropped = frame[starty:endy, startx:endx]
    decoded_objects = decode(cropped)
    for obj in decoded_objects:
        return obj.data.decode("utf-8")  # Return first QR code found

    return None  # No QR code found

# Example coordinates from previous code
crop_coords = (100, 100, 400, 400)  # (startx, starty, endx, endy)
qr_data = crop_and_scan_qr(crop_coords)
print(qr_data if qr_data else "No QR code found.")
