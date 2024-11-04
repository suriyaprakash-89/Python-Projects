from barcode import ISBN13
from barcode.writer import ImageWriter
from PIL import Image
import os

def generate_and_display_barcode(number, file_name="bar_code"):
    img_path = f"{file_name}.png"  # Initialize img_path at the start
    try:
        # Generate barcode and save as PNG
        bar_code = ISBN13(number, writer=ImageWriter())
        bar_code.save(file_name)

        # Displaying image using Pillow
        img = Image.open(img_path)
        img.show()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Remove the generated barcode file after displaying, if it exists
        if os.path.exists(img_path):
            os.remove(img_path)

# Passing 12-digit string as argument
# Valid ISBN-13 number starting with 978
num = '9780134190440'
generate_and_display_barcode(num)
