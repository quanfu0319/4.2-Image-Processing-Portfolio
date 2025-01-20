
import cv2 

img = input("please enter the file name: ")
img = cv2.imread(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #灰階
img_blur = cv2.bilateralFilter(img_gray, 5, 100, 100)   #模糊
ret, img_thsh = cv2.threshold(img_blur, 74, 255, cv2.THRESH_TOZERO) #二值化，使植物、細節變模糊。 when value < 80，make value = 0
output = cv2.Canny(img_thsh, 150, 150) 

cv2.imshow("original", img)
cv2.imshow("after", output)
cv2.imwrite('output.jpg', output) #寫入檔案
cv2.waitKey(0)

#模糊 https://medium.com/@lyxmaple/python%E7%AD%86%E8%A8%98-opencv-3-e02fa6761f0
#二值化 <127(深色) = 0(黑) https://steam.oxxostudio.tw/category/python/ai/opencv-threshold.html
#數字越大，邊緣越少 https://steam.oxxostudio.tw/category/python/ai/opencv-edge-detection.html
