import pyscreenshot as ImageGrab
import time
import pytesseract
from PIL import Image
import pyautogui

time.sleep(2)


# part of the screen
im=ImageGrab.grab(bbox=(557,444,1400,570))

# to file
im.save('img.png')
image = Image.open('img.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image).replace('change display format', "").replace("\n", " ")

print(text)

pyautogui.write(text, interval=0.05)