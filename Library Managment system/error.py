import pyautogui
import tkinter as tk
root=tk.Tk()
from PIL import Image
from pyscreenshot import grab

img = grab(bbox=(100, 200, 300, 400))

# to keep the aspect ratio
w = 300
h = 400
maxheight = 600
maxwidth = 800
ratio = min(maxwidth/width, maxheight/height)
# correct image size is not #oldsize * ratio#

# img.resize(...) returns a resized image and does not effect img unless
# you assign the return value
img = img.resize((h * ratio, width * ratio), Image.ANTIALIAS)

# Define fuction to take screenshot
myButton = tk.Button(text='Take Sscreenshot', bg='green',fg='white',font= 10)

root.mainloop()