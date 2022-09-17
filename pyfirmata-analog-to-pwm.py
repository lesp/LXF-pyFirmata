from pyfirmata2 import Arduino
import time
global pwm

PORT = Arduino.AUTODETECT
board = Arduino(PORT)
pwm = board.get_pin('d:6:p')
class Analog_To_PWM:
    def __init__(self):
        self.samplingRate = 10
        self.board = Arduino(PORT)

    def start(self):
        self.board.analog[0].register_callback(self.myPrintCallback)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[0].enable_reporting()

    def myPrintCallback(self, data):
        print("A0 reads,%f" % (round(data,1)))
        pwm.write(round(data,1))

    def stop(self):
        self.board.samplingOff()
        self.board.exit()

analog_to_pwm = Analog_To_PWM()
try:
    analog_to_pwm.start()
except:
    analog_to_pwm.stop()
