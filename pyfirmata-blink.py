import pyfirmata2
import time
PORT =  pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)

for i in range(10):
    board.digital[6].write(1)
    time.sleep(0.2)
    board.digital[6].write(0)
    time.sleep(0.2)

pwm = board.get_pin('d:6:p')
v = float(input("PWM duty cycle from 0 to 100: ")) / 100.0
pwm.write(v)
time.sleep(5)
pwm.write(0)
board.exit()