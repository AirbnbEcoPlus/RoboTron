import RPi.GPIO as GPIO




def up():
    print("Go up")
    GPIO.output(40, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    GPIO.output(36, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)

def down():
    print('Go Down')
    GPIO.output(40, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    GPIO.output(36, GPIO.HIGH)
    GPIO.output(38, GPIO.HIGH)

def TurnLeft():
    print('Go Left')
    GPIO.output(40, GPIO.HIGH)
    GPIO.output(32, GPIO.LOW)
    GPIO.output(36, GPIO.HIGH)
    GPIO.output(38, GPIO.LOW)

def TurnRight():
    print('Go Right')
    GPIO.output(40, GPIO.LOW)
    GPIO.output(32, GPIO.HIGH)
    GPIO.output(36, GPIO.LOW)
    GPIO.output(38, GPIO.HIGH)


