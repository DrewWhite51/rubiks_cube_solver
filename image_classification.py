import cv2
import tkinter as tk
from PIL import Image, ImageTk


def determine_picture_type(image_relative_path: str):
    pass

def resize_image(image_url: str, image_name = None):
    '''
    rtype: None - 
    '''
    if image_name:
        image_name_save = image_name
    else:
        image_name_save = 'image'

    if image_url:
        print(image_url)
    else:
        return None # If this happens can't really do anything because no pic was provided.
    # original_image = Image.open("assorted_shapes.jpg")

    # # Calculate the new height while preserving the aspect ratio
    # width, height = original_image.size
    # aspect_ratio = float(height) / width
    # new_width = 500
    # new_height = int(round(new_width * aspect_ratio))


    # # Resize the image and save it to a file
    # resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
    # resized_image.save("output.png")


def classify_square(image_url: str):
    # Load the image
    image = cv2.imread(image_url)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to create a binary mask
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Find contours in the binary mask
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours and filter out non-square objects
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                # This contour is a square object
                cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Convert the image from OpenCV format to PIL format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)

    # Create a new Tkinter window
    root = tk.Tk()

    # Convert the PIL image to a Tkinter PhotoImage and display it in a label
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()

    # Start the Tkinter event loop
    root.mainloop()

    # Release the OpenCV window resources
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # classify_square("pictures/assorted_shapes.jpg")
    resize_image("pictures/assorted_shapes.jpg")
    print('-----------------------------')
    resize_image("pictures/assorted_shapes.jpg")