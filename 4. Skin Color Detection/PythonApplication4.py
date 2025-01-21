import cv2
import numpy as np
from matplotlib import pyplot as plt

def iou(img, img_gt):
    img = np.array(img)
    img_gt = np.array(img_gt)
    
    interArea = np.sum(np.logical_and(img, img_gt))
    union = np.sum(np.logical_or(img, img_gt))
    
    output = interArea / union

    return(output)

sum = 0 #sum of IOU
for i in range(0, 6):
    img = cv2.imread("pic" + str(i+1) + ".jpg" )
    gt = cv2.imread("pic" + str(i+1) + ".png") # GroundTruth
    #hsv
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_mask = cv2.inRange(hsv_img, (0, 40, 120), (17, 180, 255) )
       
    #ycrcb
    img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    ycrcb_mask = cv2.inRange(img_ycrcb, (0, 133, 83), (255,182,133)) 
        
    #mix
    mix_mask=cv2.bitwise_and(ycrcb_mask,hsv_mask)
    mix_mask=cv2.medianBlur(mix_mask,3)
    mix_img = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mix_mask )
    
    #iou
    iou_value = iou(mix_img, gt)
    sum += iou_value
    print(iou_value)
    
    #output
    imgs = np.hstack( [img, mix_img] )
    cv2.imshow("", imgs)
    cv2.waitKey()
print("average: ", sum / 6)
