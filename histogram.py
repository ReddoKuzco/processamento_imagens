import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("wallpaper_life.jpg",cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result_hist = np.zeros(256, dtype=int)
for line in gray:
    for pix in line:
        result_hist[pix] += 1

plt.plot(result_hist)
plt.show()

