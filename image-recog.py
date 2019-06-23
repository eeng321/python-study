import numpy as np, matplotlib.pyplot as plt, PIL
from PIL import Image

img = Image.open(r"C:\Users\eeng\Documents\python-study\resources\kayak-lake.jpg")
imgar = np.asarray(img)

plt.imshow(imgar)
plt.show()

