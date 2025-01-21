# -*- coding: utf-8 -*-
import cv2
import numpy as np

def classification(contours):
    num_big = 0 #計算大木圓榫數量
    num_small = 0 #計算小木圓榫數量
    set_big = [] #set_contourArea
    set_small = []
            
    for i in range( len(contours) ):
        area = cv2.contourArea(contours[i]) #cv2.contourArea(物件): 可取得物件之面積，單位是pixel
        #print("current contour's area", area) #由此得知，小木圓榫之最大面積約為600 pixel
        if area > 610:
            set_big.append( contours[i] ) #contours[i]為point形成的集合
            num_big += 1
        else:
            set_small.append( contours[i] )
            num_small += 1
    
    return num_big, num_small, set_big, set_small

img = cv2.imread("wood-dowels.tif")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 轉為灰色圖片

img_gray = cv2.GaussianBlur(img_gray,(3,3),0) # 模糊消除圓形內的雜訊
ret, img_thsh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) #大津二值化，自動計算最佳閥值

kernel = np.ones((13,13), np.uint8) #侵蝕
img_e = cv2.erode(img_thsh, kernel)

kernel = np.ones((6,6), np.uint8) #膨脹
img_d = cv2.dilate(img_e, kernel)

# 找到輪廓
"""
contours: 一組向量，有多少輪廓，contours 向量内就有多少元素
hierarchy: 一組向量，hierarchy[i][0] ~ hierarchy[i][3] 分别表示第 i 個輪廓的後一個輪廓、前一個輪廓、父輪廓、内嵌輪廓的索引編號
cv2.RETR_EXTERNAL: 只檢測最外層輪廓，不檢測内層輪廓
cv2.CHAIN_APPROX_NONE: 保存物體邊界上的所有輪廓點到 contours 向量内
"""
contours, hierarchy = cv2.findContours(img_d, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

num_big, num_small, set_big, set_small = classification(contours)

#以不同顏色標示大、小木圓榫
"""
第一個參數-image：指明在哪張圖片上繪製輪廓
#第二個參數-contours：需放入輪廓之集合，且須為list
#第三個參數-contourIdx：繪製list中的哪條輪廓，-1表示繪製全部輪廓
第四個參數：欲繪製之輪廓顏色
第五個參數：欲繪製之輪廓粗度
"""
output = cv2.drawContours(img, set_big, -1, (0,0,255), 5) #大木圓榫用紅色標示
output = cv2.drawContours(output, set_small, -1, (0,255,0), 5) #小木圓榫用綠色標示

print("big", num_big)
print("small", num_small)
cv2.imshow("Result", output)

cv2.waitKey(0)