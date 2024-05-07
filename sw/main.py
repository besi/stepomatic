# ADC
from machine import ADC
adc = ADC(0)
print(adc.read())


# Neopixel does not currently work
import neopixel
from machine import Pin
np = neopixel.NeoPixel(Pin(16),1)
np.fill((100,100,100))
np.write()


# Read temperature and Humidity
from machine import Pin, SoftI2C
from hdc1080 import HDC1080

scl = Pin(5, Pin.IN, Pin.PULL_UP)
sda = Pin(4, Pin.IN, Pin.PULL_UP)
i2c = SoftI2C(scl,sda)
temp = HDC1080(i2c)
print(temp.temperature())
print(temp.humidity())


# Nod hello
import machine
import time
from machine import Pin

from uln2003 import Stepper, HALF_STEP, FULL_STEP, FULL_ROTATION
from machine import Pin

stepper = Stepper(HALF_STEP, Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT), delay=.003 )  
mode = Pin(0, Pin.IN)

ROTATIONS = 1.33333
MARGIN = 0.9
ACTIVE = 0

dir = 1
stepper.step(FULL_ROTATION/10, dir)
dir = dir * -1
stepper.step(FULL_ROTATION/10, dir)

while True:
    # Rotate in steps
    # Change direction when button is pressed
    stepper.step(FULL_ROTATION/10, dir)
    time.sleep(1)
    if mode() == ACTIVE:
        print("Mode pressed: Change direction")
        dir = dir * -1
        time.sleep(0.4) # debounce
        
