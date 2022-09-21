from pdf2image import convert_from_path
import numpy as np
from PIL import Image
import cv2

image = cv2.imread("address_here")       
# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define yellow color range
dark_yellow = np.array([72,0,221])
light_yellow = np.array([123,65,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, dark_yellow, light_yellow)
final_mask=cv2.bitwise_or(image,image,mask=mask)

# Bitwise-AND mask and original image
# output = cv2.inRange(image,image, mask= mask)
    
# cv2.imshow("Color Detected", mask)
cv2.imwrite("address_here",final_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
