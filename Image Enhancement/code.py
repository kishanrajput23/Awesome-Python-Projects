import cv2;
img = cv2.imread("input.png") 
clahe = cv2.createCLAHE()
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enh_img = clahe.apply(gray_img)
cv2.imwrite('enhanced.png',enh_img)
print("done enhancement")

