# QR Code Generator using python

## What is a QR code?

QR codes are used to encode and decode the data into a machine-readable form. The use of camera phones to read two-dimensional barcodes for various purposes is currently a popular topic in both types of research and practical applications. #

### Steps:

1. To generate QR Codes with Python you need to install only one Python library for this task:

> pip install pyqrcode

2. Now let’s see how to create a QR Code with Python programming language

```{python3}
import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code

s = "https://github.com/laxmanbalaraman/"

# Generate QR code

url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"

url.svg("myQr.svg", scale = 8)
```

3. View the Qr file that must be save in your current directory

![myQr](https://user-images.githubusercontent.com/67074796/193398963-a7d78e27-3839-45ca-9664-e04ed3708f40.svg)

**Viola you have successfully created a QR code you using python!!**
