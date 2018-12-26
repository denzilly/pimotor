import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#output pins
pins = [17,18,22,23]


def initialize():
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 1)


initialize()

a_pin = 2
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 0)

time.sleep(1)

sequence = [ [0,1,1,1],
             [0,0,1,1],
             [1,0,1,1],
             [1,0,0,1],
             [1,1,0,1],
             [1,1,0,0],
             [1,1,1,0],
             [0,1,1,0], ]

sequence2 =  [ [1,0,1,1],
             [1,0,1,0],
             [1,1,1,0],
             [0,1,1,0],
             [0,1,1,1],
             [0,1,0,1],
             [1,1,0,1],
             [1,0,0,1], ]


step_count = 128

for pin in pins:
    print("Pin %s status is: " % (str(pin)) + str(GPIO.input(pin)))



GPIO.output(2, 1)

print("Activator pin is live!")

time.sleep(2)

count = 0

speeds = [.004, .003, .002, .0012]

for x in speeds:
    for i in range(step_count):
        for half_step in range(8):
            for pin in range(4):
                GPIO.output(pins[pin], sequence2[half_step][pin])
            #for pin in pins:
                #print("Pin %s status is: " % (str(pin)) + str(GPIO.input(pin)))    
            time.sleep(x)

initialize()

print(count)

print("Sequence Complete")

GPIO.output(2,0)

print("Activation pin disabled")
GPIO.cleanup()        
