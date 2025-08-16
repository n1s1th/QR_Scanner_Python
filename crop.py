import cv2

def main():
    cap = cv2.VideoCapture(0)
    crop_width, crop_height = 300, 300  # Initial crop size

    print("Align the crop rectangle as desired. Press SPACE to output dimensions and position, 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        # Center coordinates for cropping
        startx = w // 2 - crop_width // 2
        starty = h // 2 - crop_height // 2
        endx = startx + crop_width
        endy = starty + crop_height

        # Draw rectangle
        preview_frame = frame.copy()
        cv2.rectangle(preview_frame, (startx, starty), (endx, endy), (0, 255, 0), 2)
        cv2.imshow('Crop Area Preview (SPACE=output, Q=quit)', preview_frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):
            # Output position and size
            print(f"Crop Rectangle Position and Size:")
            print(f"Top-left corner: ({startx}, {starty})")
            print(f"Bottom-right corner: ({endx}, {endy})")
            print(f"Width: {crop_width}, Height: {crop_height}")

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
