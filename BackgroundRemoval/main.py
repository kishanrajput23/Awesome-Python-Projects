import cv2 as cv
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,426)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

listImg = os.listdir("images")
# print(listImg)
imgList = []
for imgPath in listImg:
    img = cv.imread(f'images/{imgPath}')
    imgList.append(img)

# print(len(imgList))

indexImg = 0


while True:
    succ,img = cap.read()
    imgOut = segmentor.removeBG(img,imgList[indexImg],threshold=0.8)

    img_stacked = cvzone.stackImages([img,imgOut],2,1)

    _,img_stacked = fpsReader.update(img_stacked,color=(0,0,255))

    cv.imshow("Image Stacked",img_stacked)

    key = cv.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg-=1
    elif key == ord('d'):
        if indexImg<len(imgList)-1:
            indexImg+=1
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()