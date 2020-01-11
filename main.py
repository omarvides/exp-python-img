from PIL import Image
im = Image.open("py.jpg")

im.thumbnail((200, 200))
im.save("thumbnail.jpg", "JPEG")