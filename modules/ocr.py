""" An OCR for Yoruba text recognition built with Tesseract

> Performed using Google's Tesseract and the Pytesseract API

### Installing Tesseract-ocr and Pip Dependencies

The Tesseract binary is required before any tesseract related functionalities can be used.
"""

### Importing the required libraries

import cv2
import pytesseract
# from langdetect import detect_langs
# detect_langs(output_text)

## Test One: Performing OCR on computer printed text

# Show the sample images that we will work on
image_dir = "../images"
image = "whit-loc2.png"

def perform_ocr(image_dir, image):
  # custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  x_config = r"-l eng+yor -c page_separator=''"
  im = cv2.imread(f'{image_dir}/{image}')
  img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
  output = pytesseract.image_to_string(img_rgb, config=x_config)
  print(output)

  return output

output_text = perform_ocr(image_dir, image)
print(output_text)