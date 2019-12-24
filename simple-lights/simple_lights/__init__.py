import time
import RPi.GPIO as GPIO


def start_lighting(time=time, gpio=GPIO):
    gpio.setmode(GPIO.BCM)
    gpio.setwarnings(False)
    gpio.setup(18, GPIO.OUT)
    print("LED on")

    gpio.output(18, GPIO.HIGH)
    time.sleep(1)

    print("LED off")
    gpio.output(18, GPIO.LOW)


if __name__ == "__main__":
    start_lighting()