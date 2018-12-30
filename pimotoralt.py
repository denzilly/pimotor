import time
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)

orange1 = 17
yellow2 = 27
pink3 = 18
blue4 = 23

GPIO.setup(orange1, GPIO.OUT)
GPIO.setup(yellow2, GPIO.OUT)
GPIO.setup(pink3, GPIO.OUT)
GPIO.setup(blue4, GPIO.OUT)

forward_seq = ['1000', '1100', '0100', '0110', '0010', '0011', '0001', '1001']
reverse_seq = list(foward_seq).reverse()


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

def forwards(delay,steps):



    for i in range(steps):
        for step in forward_seq:
            set_step(step)
            time.sleep(delay)

def backwards(delay,steps):


    for i in range(steps)
        for step in reverse_seq:
            set_step(step)
            time.sleep(delay)

def set_step(step):
    GPIO.output(orange1, step[0] == '1')
    GPIO.output(yellow2, step[1] == '1')
    GPIO.output(pink3, step[2] == '1')
    GPIO.output(blue4, step[3] == '1')

while True:
    set_step('0000')
    delay = float(input("Delay between steps?"))
    steps = int(input("How many steps forwards?"))
    forwards(delay, steps)
    set_step('0000')
    steps = int(input("How many steps backwards?"))
    backwards(delay, steps)






print(reverse_seq)
