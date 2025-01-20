
import cv2 

img = input("please enter the file name: ")
img = cv2.imread(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #�Ƕ�
img_blur = cv2.bilateralFilter(img_gray, 5, 100, 100)   #�ҽk
ret, img_thsh = cv2.threshold(img_blur, 74, 255, cv2.THRESH_TOZERO) #�G�ȤơA�ϴӪ��B�Ӹ`�ܼҽk�C when value < 80�Amake value = 0
output = cv2.Canny(img_thsh, 150, 150) 

cv2.imshow("original", img)
cv2.imshow("after", output)
cv2.imwrite('output.jpg', output) #�g�J�ɮ�
cv2.waitKey(0)

#�ҽk https://medium.com/@lyxmaple/python%E7%AD%86%E8%A8%98-opencv-3-e02fa6761f0
#�G�Ȥ� <127(�`��) = 0(��) https://steam.oxxostudio.tw/category/python/ai/opencv-threshold.html
#�Ʀr�V�j�A��t�V�� https://steam.oxxostudio.tw/category/python/ai/opencv-edge-detection.html
