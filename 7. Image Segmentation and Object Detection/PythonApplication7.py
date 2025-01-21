import cv2
import numpy as np

def detect_desks(image, contours):
    min_area = 10000
    for contour in contours:
        if cv2.contourArea(contour) > min_area:
            peri = cv2.arcLength(contour, True)
            epsilon = 0.02 * peri #內縮輪廓之精度
            approx = cv2.approxPolyDP(contour, epsilon, True) # 回傳輪廓內縮後的頂點
            if len(approx) == 4:
                (x, y, w, h) = cv2.boundingRect(approx)
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                for point in approx: #顯示桌角
                    cv2.circle(image, tuple(point[0]), 10, (0, 0, 255), -1)
    
    return image

for i in range(2):
    file_name = "image" + str(i+1) + ".jpg"
    img = cv2.imread(file_name)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    min_hsv = (17,13,117)
    max_hsv = (40, 140, 240)
    mask = cv2.inRange(hsv, min_hsv, max_hsv)
    blur = cv2.GaussianBlur(mask, (9,9), 0)

    kernel = np.ones((19,19), np.uint8)
    opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel )

    contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = detect_desks(img, contours)

    cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Output", 800,600)
    cv2.imshow("Output", output)
    cv2.waitKey(0)