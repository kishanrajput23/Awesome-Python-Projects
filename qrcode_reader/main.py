import cv2

def read_qrcode(filename):
  try:
    img = cv2.imread(filename)
    detect = cv2.QRCodeDetector()
    value,points, straight_qrcode = detect.detectAndDecode(img)
    return value
  except:
    return None
  
value = read_qrcode("qrcode.png")
print(value)