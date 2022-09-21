from pdf2image import convert_from_path
import numpy as np
from PIL import Image
import cv2

image = cv2.imread("address_here")       
# Convert BGR to HSV
for i in range(0,10):
    for j in range(0,10):
        image[i][j]=[0,0,0]


# cv2.imshow("pixel deletion",image)
    
# cv2.imshow("Color Detected", mask)
cv2.imwrite("address_here",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
