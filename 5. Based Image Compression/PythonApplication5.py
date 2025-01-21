from PIL import Image
import os

def img_to_array(img, w, h):
    lst = [] #list
    for i in range(h):
        for j in range(w):
            lst.append(img.getpixel( (j,i) ) ) #lst���@���}�C�Alst[0]��[r,g,b]
            
    return lst
def RLE(lst):
    rle = bytearray()
    rep = 1 #repeat
    for i in range( len(lst) ):
        if i+1 != len(lst): #��e�������O�̫�@�ӹ���
            if lst[i] == lst[i+1]: #�۾F�⹳����rgb�ۦP
                rep+=1
                if rep > 255:
                    rep = 255
                    rle.append(rep)
                    rle.extend(lst[i])
                    rep = 1
            else: #�۾F�⹳����rgb���P�A��JRLE list
                rle.append(rep) #rle���G���}�C�Arle[0][0]���`�ơArle[0][1]��[r,g,b]
                rle.extend(lst[i])
                rep = 1
        else: #��e�������̫�@�ӹ���
            rle.append(rep)
            rle.extend(lst[i])
 
    return rle
def unzip(rleFile):
    img_data = bytearray()
    
    i = 0
    while i < len(rleFile):
        count = rleFile[i]
        color = rleFile[i+1:i+4]
        img_data.extend(color * count)
        i += 4
        
    return img_data

sum_compression_ration = 0

for i in range(3):
    pic_name = "img" + str(i+1) + ".bmp"
    img = Image.open(pic_name)
    w, h = img.size

    rgb_arr = img_to_array(img, w, h)
    rle_arr = RLE(rgb_arr)
    
    fileName = "compressed_data" + str(i+1) +".bin"
    f = open(fileName, "wb")
    f.write(rle_arr)
    f.close()
    
    img_data = unzip(rle_arr)
    img2 = Image.frombytes("RGB", (w,h), bytes(img_data) )
    
    size_original = os.path.getsize(pic_name)
    size_rle = os.path.getsize(fileName)
    temp = size_original / size_rle
    sum_compression_ration += temp
    print("original size:", size_original)
    print("after rle size:", size_rle)
    print("compression ratio:", temp, "\n")
    
    img2.show()
print("average compression ration:", sum_compression_ration / 3)
