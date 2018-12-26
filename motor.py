import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#output pins
pins = [17,18,22,23]
a_pin = 2


#Initialize motor driver GPIO pins to state 1 (L293D IC interprets 1 as zero state)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

#Initialize enable pin to state 0
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 0)


time.sleep(1)



#These are the pulse sequences that define how the motor turns, in half steps

sequence_ccw =  [ [1,0,1,1],
             [1,0,1,0],
             [1,1,1,0],
             [0,1,1,0],
             [0,1,1,1],
             [0,1,0,1],
             [1,1,0,1],
             [1,0,0,1], ]

sequence_cw =  [ [1,0,0,1],
             [1,1,0,1],
             [0,1,0,1],
             [0,1,1,1],
             [0,1,1,0],
             [1,1,1,1],
             [1,0,1,0],
             [1,0,1,1], ]




for pin in pins:
    print("Pin %s status is: " % (str(pin)) + str(GPIO.input(pin)))



GPIO.output(2, 1)

print("Activator pin is live!")

time.sleep(2)

rot = float(input("How many degrees of rotation?"))
spd = float(input("Rotation speed? (time between pulses)"))
di = input("Direction of rotation? (cw or ccw)")


if (di == "cw"):
    direction = sequence_cw
else:
    direction = sequence_ccw
    
step_count = round(rot/2.8125)

for i in range(step_count):
    for half_step in range(8):
        for pin in range(4):
            GPIO.output(pins[pin], direction[half_step][pin])
        #for pin in pins:
            #print("Pin %s status is: " % (str(pin)) + str(GPIO.input(pin)))
        time.sleep(spd)



print("Sequence Complete")

GPIO.output(2,0)

print("Activation pin disabled")
GPIO.cleanup()
