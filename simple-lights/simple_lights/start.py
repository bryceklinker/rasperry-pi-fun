from gpiozero import LED
from time import sleep

pin_18_led = LED(18)
pin_17_led = LED(17)

while True:
    pin_17_led.off()
    pin_18_led.on()
    sleep(1)
    pin_17_led.on()
    pin_18_led.off()
    sleep(1)
