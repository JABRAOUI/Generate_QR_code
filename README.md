# 📷 QR Code Generator with Custom Title

This Python script generates a **QR code from any user-provided text**, and saves it as an image with a **custom title header**. It's interactive, simple to use, and requires no external web services.

---

## 🎯 Features

* ✅ Generates QR codes for any text (URLs, messages, contact info, etc.)
* 🖼️ Adds a title above the QR code image
* 📁 Saves to `.png`, `.jpg`, or `.jpeg` formats
* 🔍 Prevents overwriting existing files
* 🔠 Uses system fonts (fallback to default if unavailable)

---

## 🛠️ Requirements

* Python 3.x
* [qrcode](https://pypi.org/project/qrcode/)
* [Pillow (PIL)](https://pypi.org/project/Pillow/)

### Install dependencies:

```bash
pip install qrcode[pil] Pillow
```

---

## 🚀 How to Use

### Run the script:

```bash
python qr_generator.py
```

### You'll be prompted to:

1. **Enter the text** you want to encode (e.g., a message or a URL).
2. **Specify a filename** to save the QR code (e.g., `my_qrcode.png`).

If the file already exists, you'll be asked to choose another name.

---

## 🧾 Example

```
Welcome to the QR Code Generator!
=================================

Please leave a message:
> https://github.com/yourusername/qr-generator

Please enter the filename to save the QR code:
> github_qr.png

Success! Your QR code has been saved as 'github_qr.png'.
You can find it in: /your/path/github_qr.png
```

---

## 🔧 Configuration (Optional)

You can change the title or QR settings by editing the script:

```python
draw.text((10, 10), "Your QR Code", font=font, fill="black")  # <-- Change the title here

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
```

---

## 💡 Use Cases

* Personal or academic project links
* Wi-Fi credentials or contact info
* Event invites or promotional materials
* Securely share short messages

---

## 📃 License

MIT License. Free to use, modify, and distribute.

---

## 📁 Example Output

Here’s what the final QR image looks like (with a custom title):

```
+-------------------------+
|      Your QR Code      |
+-------------------------+
|         [ QR CODE ]     |
+-------------------------+
```

Let me know if you want to:

* Add a GUI version
* Customize QR colors and background
* Automatically email or upload the generated QR
