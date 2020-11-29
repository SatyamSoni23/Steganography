import cv2
import numpy as np
img=cv2.imread("nobita.jpg")
img=cv2.resize(img, (300,300))
height, width, channels = img.shape
blank_image = np.zeros(shape=[300, 300, 3], dtype=np.uint8)
white = [255,255,255]
black = [0,0,0]


u=60
v=60
a=0
b=0
c = int(u/3)
for x in range(a+0,int(u/3)):
    for y in range(b+0,int(v/3)):
        blank_image[c+y, c+x] = img[y, x]
        
for x in range(a + int(u/3),a + int((2*u)/3)):
    for y in range(b + 0,b + int(v/3)):
        blank_image[c+y, x - c]= img[y, x] 
                
for x in range(a + 0,a + int(u/3)):
    for y in range(b + int(v/3),b + int((2*v)/3)):
        blank_image[y-c, x +c] = img[y, x]
        
for x in range(a + int(u/3), + int(2*u/3)):
    for y in range(b + int(v/3),b + int(2*v/3)):
        blank_image[y-c, x - c] = img[y, x]

for x in range(a + int(2*u/3),a + int(3*u/3)):
    for y in range(b + 0, b + int(v/3)):
        blank_image[y+c, x] = img[y, x]

for x in range(a + int((2*u)/3), a + int(3*u/3)):
    for y in range(b + int(v/3),b + int(2*v/3)):
        blank_image[y-c, x] = img[y, x]
        
for x in range(a + 0, a + int(u/3)):
    for y in range(b + int(2*v/3), b + int(3*v/3)):
        blank_image[y, x+c] = img[y, x]

for x in range(a + int(u/3),a + int(2*u/3)):
    for y in range(b + int(2*v/3), b + int(3*v/3)):
        blank_image[y, x-c] = img[y, x]
        
for x in range(a + int(2*u/3), a + int(3*u/3)):
    for y in range(b + int(2*v/3), b + int(3*v/3)):
        blank_image[y, x] = img[y, x]   
        



u=60
v=60
a=0
b=60
c = int(u/3)
for x in range(a + 0,a + int(u/3)):
    for y in range(b + 0, b + int(v/3)):
        blank_image[c+y, c+x] = img[y, x]
        
for x in range(a + int(u/3),a + int((2*u)/3)):
    for y in range(b + 0,b + int(v/3)):
        blank_image[c+y, x - c]= img[y, x] 
                
for x in range(a + 0,a + int(u/3)):
    for y in range(b + int(v/3),b + int((2*v)/3)):
        blank_image[y-c, x +c] = img[y, x]
        
for x in range(a + int(u/3), + int(2*u/3)):
    for y in range(b + int(v/3),b + int(2*v/3)):
        blank_image[y-c, x - c] = img[y, x]

for x in range(a + int(2*u/3),a + int(3*u/3)):
    for y in range(b + 0, b + int(v/3)):
        blank_image[y+c, x] = img[y, x]

for x in range(a + int((2*u)/3), a + int(3*u/3)):
    for y in range(b + int(v/3),b + int(2*v/3)):
        blank_image[y-c, x] = img[y, x]
        
for x in range(a + 0, a + int(u/3)):
    for y in range(b + int(2*v/3), b + int(3*v/3)):
        blank_image[y, x+c] = img[y, x]

for x in range(a + int(u/3),a + int(2*u/3)):
    for y in range(b + int(2*v/3), b + int(3*v/3)):
        blank_image[y, x-c] = img[y, x]
        
for x in range(a + int(2*u/3), a + int(3*u/3)):
    for y in range(b + int(2*v/3), b + int(3*v/3)):
        blank_image[y, x] = img[y, x]           

       
cv2.imshow('img',blank_image)
cv2.imshow('im', img)
cv2.waitKey(0)
cv2.destroyAllWindows()                