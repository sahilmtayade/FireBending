import os

import cv2


def list_mp4_files():
    # Get a list of MP4 files in the current directory
    mp4_files = [file for file in os.listdir() if file.endswith(".mp4")]

    if not mp4_files:
        print("No MP4 files found in the current directory.")
        return None

    # Print the list of MP4 files with corresponding numbers
    print("MP4 files in the current directory:")
    for i, mp4_file in enumerate(mp4_files, start=1):
        print(f"{i}. {mp4_file}")

    # Prompt the user to choose a file by entering a number
    while True:
        try:
            choice = int(input("Enter the number of the MP4 file you want to use: "))
            if 1 <= choice <= len(mp4_files):
                return mp4_files[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def pick_center(image):
    # Create a window
    cv2.namedWindow("Pick Center", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Pick Center", 800, 600)

    # Set a callback function to get the coordinates when a mouse click occurs
    center_coordinates = []

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            center_coordinates.append((x, y))
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("Pick Center", image)

    cv2.setMouseCallback("Pick Center", mouse_callback)

    # Display the image
    cv2.imshow("Pick Center", image)

    # Wait for the user to click
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return center_coordinates[0] if center_coordinates else None


if __name__ == "__main__":
    # List MP4 files and allow the user to choose one
    selected_mp4 = list_mp4_files()

    if selected_mp4:
        # Load the selected MP4 video
        video_path = os.path.join(os.getcwd(), selected_mp4)
        video_capture = cv2.VideoCapture(video_path)

        # Prompt the user to specify the frame to view
        frame_number = int(
            input(
                f"Enter the frame number to view (1 to {int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))}): "
            )
        )

        # Set the capture object to the specified frame
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)

        # Read the specified frame
        ret, frame = video_capture.read()

        if ret:
            # Get the center coordinates
            center = pick_center(frame)

            if center:
                print("Center Coordinates:", center)
            else:
                print("No center coordinates selected.")
        else:
            print("Error reading the specified frame.")
