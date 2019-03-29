from PIL import Image, ImageFilter

file="dis.jpg"

image = Image.open(file)
box = (30, 30, 100, 100)
crop_img = image.crop(box)
# Use GaussianBlur directly to blur the image 10 times. 
blur_image = crop_img.filter(ImageFilter.GaussianBlur(radius=20)).show()
