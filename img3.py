from PIL import Image,ImageFilter

file = "girl.jpg"

image = Image.open(file)
image.filter(ImageFilter.BLUR).show()
image.filter(ImageFilter.CONTOUR).show()
image=Image.open(file).show()