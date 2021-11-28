import numpy as np
from PIL import Image, ImageOps
img1 = Image.open("flower.jpg")
img1 = ImageOps.grayscale(img1)
img2 = Image.open("output/flower-decrypt-crop.png")
Y = np.square(np.subtract(img1,img2)).mean()
print("MSE:", Y)