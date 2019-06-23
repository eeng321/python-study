from PIL import Image

img = Image.open(r"C:\Users\eeng\Documents\python-study\resources\kayak-lake.jpg")

print(img.size)
width, height = img.size

img.show()