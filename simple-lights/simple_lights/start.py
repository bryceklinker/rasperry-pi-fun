from gpiozero import LED
from time import sleep

pin_18_led = LED(18)

while True:
    pin_18_led.on()
    sleep(1)
    pin_18_led.off()
    sleep(1)