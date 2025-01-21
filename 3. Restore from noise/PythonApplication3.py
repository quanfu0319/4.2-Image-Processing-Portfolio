import cv2
import numpy as np
from matplotlib import pyplot as plt

def median_filter(image, kernel_size):
    pad = (kernel_size-1) // 2 #中位數濾波器的邊界
    
    filtered_image = np.zeros_like(image) #零填充的圖片，用以儲存結果
    
    rows, cols = image.shape
    
    for i in range(pad, rows - pad):
        for j in range(pad, cols - pad):
            window = image[i-pad:i+pad+1, j-pad:j+pad+1] #獲取濾波器內的像素值
            filtered_image[i, j] = np.median(window) #將像素排序，取中位數
    
    return filtered_image

img = input("please enter the file name: ")
img = cv2.imread(img, 2) #2代表開啟灰階圖片

img_ft = np.fft.fft2(img) #將空間域(圖片) 透過傅立葉轉換變成頻率域(複數陣列) https://www.osgeo.cn/numpy/reference/generated/numpy.fft.fft2.html
ft = np.fft.fftshift(img_ft) #將零頻率分量移到頻譜中心 https://www.osgeo.cn/numpy/reference/generated/numpy.fft.fftshift.html

ms = np.log(np.abs(ft)) #振幅譜
ps = np.angle(ft) #相位譜 https://www.zhihu.com/question/265430352

ks = 3 #kernel size
filtered_image = median_filter(img, ks)


#印出結果
plt.subplot(221) #plt.subplot創建圖像窗口，221代表窗口分為2行2列，當前位置為1
plt.imshow(img, cmap = "gray") #若沒有cmap = "gray"則默認為綠色
plt.title("Input")
plt.axis("off") #關閉坐標軸 https://www.cnblogs.com/shuaishuaidefeizhu/p/14034415.html
#-------------------------------------------------------------------------------------
plt.subplot(223)
plt.imshow(ms, cmap = "gray") 
plt.title("Magnitude Spectrum")
plt.axis("off") 
#-------------------------------------------------------------------------------------
plt.subplot(224)
plt.imshow(ps, cmap = "gray")
plt.title("Phase Spectrum")
plt.axis("off")
#-------------------------------------------------------------------------------------
plt.subplot(222)
plt.imshow(filtered_image, cmap = "gray")
plt.title("Output")
plt.axis("off")
#-------------------------------------------------------------------------------------
cv2.imwrite("output.jpg", filtered_image)         
plt.show()

#參考
#https://blog.csdn.net/imxlw00/article/details/112917891
#https://medium.com/@mingjiehsu/%E6%BF%BE%E6%B3%A2%E5%99%A8%E5%B0%8D%E5%9C%96%E5%83%8F%E9%9B%9C%E8%A8%8A%E8%99%95%E7%90%86%E6%AF%94%E8%BC%83-%E4%B8%8B-5c0fe4d47b5