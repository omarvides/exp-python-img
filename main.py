from PIL import Image
im = Image.open("py.jpg")

# Showing information of the image imported
print(im.size)

# Creating a smaller version of the image (Square)
im.thumbnail((200, 200))
im.save("thumbnail.jpg", "JPEG")

# Cropping removing a percentage of the image based on its size
im = Image.open("py.jpg")
percent = 40
x_perc = (im.size[0] * percent / 100)
y_perc = (im.size[1] * percent / 100)
section = (0, 0, im.size[0] - x_perc, im.size[1] - y_perc)
cropped = im.crop(section)
cropped.save("cropped.jpg", "JPEG")