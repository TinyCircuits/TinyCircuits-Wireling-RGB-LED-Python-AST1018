# RGB LED Wireling Rainbow example:
# This example shows how to create a single pixel with a specific color channel
# order and go through a color feature displaying the rainbow
# Library by: Adafruit
# Hardware by: TinyCircuits

import time
import board
import neopixel
import tinycircuits_wireling

wireling = tinycircuits_wireling.Wireling() # Enables power to Pi Hat

# Configure the setup
PIXEL_PIN = wireling.getBoardPin(1) # getBoardPin() returns the pin correlating to the input port
ORDER = neopixel.GRB   # pixel color channel order
COLOR = (255, 255, 0)  # color to blink
CLEAR = (0, 0, 0)      # clear (or second color)
DELAY = 0.2            # blink rate in seconds
BRIGHT = 0.125	       # brightness

# Colors
RED = (255, 0, 0)
ORANGE = (255, 69, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRN_BLU = (0, 255, 30)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
PINK = (215, 0, 31)

# Create the NeoPixel object
pixel = neopixel.NeoPixel(PIXEL_PIN, 1, brightness=BRIGHT, pixel_order=ORDER)

# Loop forever and blink the color
while True:
    pixel[0] = RED
    time.sleep(DELAY)
    pixel[0] = ORANGE
    time.sleep(DELAY)
    pixel[0] = YELLOW
    time.sleep(DELAY)
    pixel[0] = GREEN
    time.sleep(DELAY)
    pixel[0] = GRN_BLU
    time.sleep(DELAY)
    pixel[0] = BLUE
    time.sleep(DELAY)
    pixel[0] = PURPLE
    time.sleep(DELAY)
    pixel[0] = PINK
    time.sleep(DELAY)
