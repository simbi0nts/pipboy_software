import RPi.GPIO as GPIO
from time import sleep
import os, sys

class KY040:

    CLOCKWISE = 1
    ANTICLOCKWISE = 0
    
    def __init__(self, clockPin, dataPin, switchPin,
                 rotaryCallback, switchCallback):
        #persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback

        #setup pins
        GPIO.setup(clockPin, GPIO.IN)
        GPIO.setup(dataPin, GPIO.IN)
        GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        GPIO.add_event_detect(self.clockPin,
                              GPIO.FALLING,
                              callback=self._clockCallback,
                              bouncetime=250)
        GPIO.add_event_detect(self.switchPin,
                              GPIO.FALLING,
                              callback=self._switchCallback,
                              bouncetime=300)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.switchPin)
    
    def _clockCallback(self, pin):
        if GPIO.input(self.clockPin) == 0:
            data = GPIO.input(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.CLOCKWISE)
            else:
                self.rotaryCallback(self.ANTICLOCKWISE)
    
    def _switchCallback(self, pin):
        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()

#test
if __name__ == "__main__":
    
    CLOCKPIN = 11
    DATAPIN = 13
    SWITCHPIN = 15

    def rotaryChange(direction):
	encoder = open("encoder_data.log","w")
        encoder.write(str(direction))
	encoder.close()
    def switchPressed():
	encoder = open("encoder_data.log","w")
        encoder.write("2")
        encoder.close()

    GPIO.setmode(GPIO.BOARD)
    
    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN,
                  rotaryChange, switchPressed)

    ky040.start()

    try:
        while True:
            sleep(0.1)
    finally:
        ky040.stop()
        GPIO.cleanup()
