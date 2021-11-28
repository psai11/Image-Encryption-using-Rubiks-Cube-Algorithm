import random
import cv2
 
def add_noise(img):
 
    row , col = img.shape
     
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
       
        y_coord=random.randint(0, row - 1)
         
        x_coord=random.randint(0, col - 1)
         
        img[y_coord][x_coord] = 255
         
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
       
        y_coord=random.randint(0, row - 1)
         
        x_coord=random.randint(0, col - 1)
         
        img[y_coord][x_coord] = 0
         
    return img
 
img = cv2.imread('output/eye-encrypted.png',
                 cv2.IMREAD_GRAYSCALE)
 
#Storing the image
cv2.imwrite('output/salt-and-pepper-eye-encrypted.png',
            add_noise(img))