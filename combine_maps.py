from pdf2image import convert_from_path
import numpy as np
from PIL import Image
import cv2

water_mask = cv2.imread("address_here")
city_mask = cv2.imread("address_here")

combined_mask = water_mask + city_mask

cv2.imwrite("address_here",combined_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()