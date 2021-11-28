from PIL import Image

def center_crop(img, dim):
    """Returns center cropped image
	Args:
	img: image to be center cropped
	dim: dimensions (width, height) to be cropped
	"""
    width, height = img.size
    # print(img.shape)

	# process crop width and height for max available dimension
    crop_width = dim[0] if dim[0]<height else height
    crop_height = dim[1] if dim[1]<width else width
    mid_x, mid_y = int(width/2), int(height/2)

    crop_img = img

    for i in range((mid_x-crop_width//2),(mid_x+crop_width//2)):
        for j in range((mid_y-crop_height//2),(mid_y+crop_height//2)):
            crop_img.putpixel((i,j),0)
	
    return crop_img

if __name__ == "__main__":
    image = Image.open('eye-encrypted.jpg')
    print(image.size)
    ccrop_img = center_crop(image, (100,100))
    ccrop_img.save("output/eye-crop.png")
    