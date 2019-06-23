#Apply multiple filters to image to have a better comparison

import matplotlib.pyplot as plt
import skimage
from skimage import io
from skimage import filters
import numpy as np
import matplotlib
matplotlib.rcParams['xtick.major.size'] = 0
matplotlib.rcParams['ytick.major.size'] = 0
matplotlib.rcParams['xtick.labelsize'] = 0
matplotlib.rcParams['ytick.labelsize'] = 0

def plot():    
    fig = plt.figure(figsize=(20, 10))
    num_img = 4
    rows = 4
    columns = 5
    for i in range(1, num_img + 1):
        img = img_arr[i]
        fig.add_subplot(rows, columns, i)
        plt.title(namestr(img_arr[i], globals()))
        plt.imshow(img)
    plt.show()

def sharpen(image, a, b, sigma=10):
    blurred = filters.gaussian(image, sigma=sigma, multichannel=True)
    sharper = np.clip(image * a - blurred * b, 0, 1.0)
    return sharper

def channel_adjust(channel, values):
    # flatten
    orig_size = channel.shape
    flat_channel = channel.flatten()
    adjusted = np.interp(
        flat_channel,
        np.linspace(0, 1, len(values)),
        values)

    # put back into image form
    return adjusted.reshape(orig_size)

def split_image_into_channels(image):
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]
    return red_channel, green_channel, blue_channel

def merge_channels(red_channel, green_channel, blue_channel):
    return np.stack([red_channel, green_channel, blue_channel], axis=2)

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def f_gotham(img):
    r, g, b = split_image_into_channels(img)
    r_adjusted = channel_adjust(r, [
        0, 0.05, 0.1, 0.2, 0.3,
        0.5, 0.7, 0.8, 0.9,
        0.95, 1.0])
    bluer_blacks = merge_channels(r_adjusted, g, np.clip(b + 0.03, 0, 1.0))
    sharper = sharpen(bluer_blacks, 1.3, 0.3, sigma=10)
    r,g,b = split_image_into_channels(sharper)
    b_adjusted = channel_adjust(b, [
        0, 0.047, 0.118, 0.251, 0.318,
        0.392, 0.42, 0.439, 0.475,
        0.561, 0.58, 0.627, 0.671,
        0.733, 0.847, 0.925, 1])
    return merge_channels(r, g, b_adjusted)

original_image = skimage.img_as_float(io.imread(r"C:\Users\eeng\Documents\python-study\resources\kayak-lake.jpg"))

img_arr = []
img_arr.append(original_image) #filler
img_arr.append(original_image)

sharper = sharpen(original_image, 1.3, 0.3)
img_arr.append(sharper)

blurred = sharpen(original_image, 0, -1.0)
img_arr.append(blurred)

gotham = f_gotham(original_image)
img_arr.append(gotham)

plot()

#save image you like