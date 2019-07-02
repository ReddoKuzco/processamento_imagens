import cv2

img = cv2.imread("modern.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 80, 200)

cv2.imshow('modern',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

from matplotlib import pyplot as plt

import numpy as np

x = np.array()
plt.show()
