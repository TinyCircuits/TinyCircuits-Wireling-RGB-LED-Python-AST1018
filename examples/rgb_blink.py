# This example shows how to create a single RGB with a specific color channel
# order and blink it.
# Library by: Adafruit
# Hardware by: TinyCircuits

import time
import board
import neopixel
import tinycircuits_wireling

wireling = tinycircuits_wireling.Wireling()


# Configure the setup
RGB_PIN = wireling.getBoardPin(1)
ORDER = neopixel.GRB   # pixel color channel order
COLOR = (150, 0, 150)  # color to blink: purple
CLEAR = (0, 0, 0)      # clear (or second color)
DELAY = 1              # blink rate in seconds

# Create the RGB Wireling object using neopixel library
pixel = neopixel.NeoPixel(RGB_PIN, 1, pixel_order=ORDER)

# Loop forever and blink the color
while True:
    pixel[0] = COLOR
    time.sleep(DELAY)
    pixel[0] = CLEAR
    time.sleep(DELAY)
