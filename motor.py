import time
import RPi.GPIO as GPIO

#output pins
pins = [17,18,22,23]
Enable_293 = 2

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







def setup():

    GPIO.setmode(GPIO.BCM)




    #Initialize motor driver GPIO pins to state 1 (L293D IC interprets 1 as zero state)

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 1)

    #Initialize enable pin to state 0
    GPIO.setup(Enable_293, GPIO.OUT)
    GPIO.output(Enable_293, 0)

    #Wait x seconds
    time.sleep(1)



########This function requests rotation, speed, and direction inputs from the user, and validates input types.
def get_params():

#define errors
    class NotPositiveError(UserWarning):
        pass
    class NotCWError(UserWarning):
        pass

#request degrees of rotation, validate input
    while True:
        try:
            rot = int(input("How many degrees of rotation?"))
            if (rot < 0):
                raise NotPositiveError
            print(rot)
            break

        except ValueError:
            print ("Please enter a positive integer value!")
            continue

        except NotPositiveError:
            print ("Your value was negative!")
            continue

        else:
            print(rot)
            break
#Request rotation speed, validate input
    while True:
        try:
            spd = float(input("Rotation speed (time between pulses .002-.5)?"))
            if (spd < 0):
                raise NotPositiveError
            break

        except ValueError:
            print ("Please enter a positive decimal value!")
            continue

        except NotPositiveError:
            print ("Your value was negative!")
            continue

#Request rotation direction, validate input
    while True:
        try:
            di = str(input("Direction of rotation? (cw or ccw)"))
            
            
            if (di != "cw") & (di != "ccw"):
                raise NotCWError

            break

        except ValueError:
            print ("Please enter ccw or cw")
            continue

        except NotCWError:
            print ("Please enter ccw or cw")
            continue

    params = [rot, spd, di]

    return params


def runmotor():


    #Check status of all pins
    for pin in pins:
        print("Pin %s status is: " % (str(pin)) + str(GPIO.input(pin)))

    print("Pin %s status is: " % (str(Enable_293)) + str(GPIO.input(Enable_293)))

    #Activate enable pin
    GPIO.output(Enable_293, 1)

    print("Enable 293D pin is live!")

    time.sleep(1)

    #Get parameters from user as list [rot, spd, di]
    params = get_params()

    if (params[2] == "cw"):
        direction = sequence_cw
    else:
        direction = sequence_ccw

    step_count = round(params[0]/2.8125)

    for i in range(step_count):
        for half_step in range(8):
            for pin in range(4):
                GPIO.output(pins[pin], direction[half_step][pin])
            #for pin in pins:
                #print("Pin %s status is: " % (str(pin)) + str(GPIO.input(pin)))
            time.sleep(params[1])

setup()
runmotor()


print("Sequence Complete")

GPIO.output(Enable_293,0)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

print("Activation pin disabled")
#input("Pause")
#GPIO.cleanup()
