import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#output pins
pins = [17,18,22,23]
Enable_293 = 2


#Initialize motor driver GPIO pins to state 1 (L293D IC interprets 1 as zero state)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

#Initialize enable pin to state 0
GPIO.setup(Enable_293, GPIO.OUT)
GPIO.output(Enable_293, 0)

#Wait x seconds
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

print("Pin %s status is: " % (str(Enable_293)) + str(GPIO.input(Enable_293)))


GPIO.output(Enable_293, 1)

print("Enable 293D pin is live!")

time.sleep(1)

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

GPIO.output(Enable_293,0)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

print("Activation pin disabled")
#input("Pause")
#GPIO.cleanup()
