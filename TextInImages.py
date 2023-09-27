import pytesseract
import numpy as np
import cv2 # OpenCV

import os
os.system('whoami')

# Load Image
img = cv2.imread(r'./images/test01.jpg')
cv2.imshow('',img)
cv2.waitKey()

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('',rgb)
cv2.waitKey()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(rgb)
print(text)

img = cv2.imread(r'./images/test02-02.jpg')
cv2.imshow('',img)
cv2.waitKey()

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('',rgb)
cv2.waitKey()

text = pytesseract.image_to_string(rgb)
print(text)

text = pytesseract.image_to_string(rgb,lang='por')
print(text)

img = cv2.imread(r'./images/page-book.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('',rgb)
cv2.waitKey()


config_tesseract = '--tessdata-dir tessdata --psm 6'
text = pytesseract.image_to_string(rgb,lang='por',config=config_tesseract)
print(text)

config_tesseract = '--tessdata-dir tessdata --psm 7'
text = pytesseract.image_to_string(rgb,lang='por',config=config_tesseract)
print(text)

img = cv2.imread(r'./images/exit.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('',rgb)
cv2.waitKey()

config_tesseract = '--tessdata-dir tessdata --psm 7'
text = pytesseract.image_to_string(rgb,lang='por',config=config_tesseract)
print(text)


from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r'./images/book01.jpg')
plt.imshow(img)
plt.show()

print(pytesseract.image_to_osd(img))