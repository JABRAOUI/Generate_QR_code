import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def create_qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    img_with_title = Image.new('RGB', (img.size[0], img.size[1] + 50), color='white')
    img_with_title.paste(img, (0, 50))
    
    draw = ImageDraw.Draw(img_with_title)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        print("Warning: 'arial.ttf' font not found. Using default font.")
        font = ImageFont.load_default()
    
    draw.text((10, 10), "Your QR Code", font=font, fill="black")

    img_with_title.save(filename)

def main():
    print("Welcome to the QR Code Generator!")
    print("=================================")

    while True:
        text = input("\nPlease leave a message:\n> ")
        if text.strip():  # Ensure the input is not empty or just whitespace
            break
        print("The text cannot be empty. Please try again.")

    while True:
        filename = input("\nPlease enter the filename to save the QR code (e.g., Yasser.png):\n> ")
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            if not os.path.exists(filename):  # Check if the file already exists
                break
            else:
                print(f"A file named '{filename}' already exists. Please choose a different name.")
        else:
            print("Please use a valid image file extension (.png, .jpg, or .jpeg).")

    create_qr_code(text, filename)

    print(f"\nSuccess! Your QR code has been saved as '{filename}'.")
    print(f"You can find it in: {os.path.abspath(filename)}")

if __name__ == "__main__":
    main()
