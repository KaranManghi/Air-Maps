from pdf2image import convert_from_path
import numpy as np
from PIL import Image
import cv2

# Image.MAX_IMAGE_PIXELS = None

sectional=convert_from_path('address_here')

for i in range(len(sectional)):
   
      # Save pages as images in the pdf
    sectional[i].save('address_here' +'.jpg', 'JPEG')

print("done")

