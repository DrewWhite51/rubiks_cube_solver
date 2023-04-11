import cv2
import tkinter as tk
from PIL import Image, ImageTk


def simple_snap_pic():
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Save the captured image to a file
    cv2.imwrite("image.jpg", frame)

    # Release the webcam
    cap.release()


def snap_pic_gui():
    
    # Create a tkinter window
    window = tk.Tk()

    # Create a label to display the captured image
    image_label = tk.Label(window)
    image_label.pack()

    # Create a button to capture the image
    capture_button = tk.Button(window, text="Capture")

    def capture_image():
        # Open the default webcam
        cap = cv2.VideoCapture(0)

        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to an RGB image
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the RGB image to a PIL Image object
        pil_image = Image.fromarray(rgb_image)

        # Convert the PIL Image object to a PhotoImage object
        photo = ImageTk.PhotoImage(pil_image)

        # Update the label to display the captured image
        image_label.configure(image=photo)
        image_label.image = photo

        # Save the captured image to a file
        pil_image.save("image.jpg")

        # Release the webcam
        cap.release()

    # Bind the capture_button to the capture_image() function
    capture_button.configure(command=capture_image)
    capture_button.pack()

    # Start the tkinter event loop
    window.mainloop()

if __name__ == '__main__':
    snap_pic_gui()