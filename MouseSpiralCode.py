from PIL import Image, ImageDraw
import time
import ctypes
import win32api
import win32con

# Set the image size
w, h = 800, 600
im = Image.new("RGB", (w, h))

# Create a line for the spiral
for i in range(w - 1):
    for j in range(h - 1):
        x, y = 0, 0
        for k in range(80 * i):
            x += int(win32api.GetMousePos(True, ctypes.byref(x), ctypes.byref(y)).x)
            y += int(win32api.GetMousePos(True, ctypes.byref(x), ctypes.byref(y)).y)
        im.putpixel((i, j), (x, y))

# Save the image
im.save("spiral.jpg", "JPEG")
