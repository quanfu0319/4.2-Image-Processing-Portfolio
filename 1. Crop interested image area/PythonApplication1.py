import cv2
#===user��J�ƾ�===
name = input("please enter the picture name: ")
cropW = int( input("width of image after cropped: ") )
cropH = int( input("height of image after cropped: ") )
#===Ū���ɮ�===
img = cv2.imread(name)
#===�ܼƫŧi===
height, width = img.shape[:2]
x,y = 0, 0
zoomW, zoomH = 0, 0
angle = 0
center = (width // 2, height // 2)
#===�禡�ϰ�===
def create_preview_window():
    cv2.namedWindow("preview window", cv2.WINDOW_NORMAL)
    if (height > 600 and width > 600): #�קKwindow�Ӥj�A���H�ޱ�
        cv2.resizeWindow("preview window", 600, 600)
    cv2.imshow("preview window", img)
    
def create_cropped_window():
    cv2.namedWindow("cropped window", cv2.WINDOW_NORMAL)   
    if (height > 600 and width > 600):
        cv2.resizeWindow("cropped window", 600, 600)

def setRec(): #�]�m�x��
    startP = (x, y)
    endP = ( int(x+zoomW), int(y+zoomH) )
    img = cv2.imread(name) #�Y�����sŪ���A�h�W��setRec���x�η|�ݯd
    cv2.rectangle(img, startP, endP, (0,0,0), 5)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    img = cv2.warpAffine(img, M, (width, height))
    
    cv2.imshow("cropped window", img)
    
def zoom(val):
    global zoomW, zoomH
    val = float(val / 100) #�ϥΪ̩԰�zoom��񪺭ȡA�q�{val==100
    zoomW = cropW * val
    zoomH = cropH * val
    setRec()
    
def rotate(val):
    global angle
    angle = val
    setRec()
    
def setX_fn(val):#�]�m���W��x�y��
    global x
    x = val
    setRec()
    
def setY_fn(val): #�]�m���W��y�y��
    global y
    y = val
    setRec()

def crop(val): #�����ɮ�
    if val == 1:
        output = img[y:int(y+zoomH), x:int(x+zoomW)]
        cv2.imshow("cropped window", output)
        cv2.imwrite('crop.jpg', output) #�g�J�ɮ�
        
#===�D�n�����===        
create_preview_window()
create_cropped_window()
#===�Ы�trackbar===
cv2.createTrackbar('Zoom', 'preview window' , 100, 500, zoom)
cv2.createTrackbar('Rotate', 'preview window', 0, 360, rotate)
cv2.createTrackbar('iniX', 'preview window' , 0, 4032, setX_fn)
cv2.createTrackbar('iniY', 'preview window', 0, 3024, setY_fn)
cv2.createTrackbar('SaveFile', 'preview window', 0, 1, crop)
#===�ϵ������d����{������===
cv2.waitKey(0)