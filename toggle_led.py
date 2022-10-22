from gpiozero import LED

led = LED(17)

toggle = input("Would you like to turn the light on or off?: ")

while True:
    if toggle == "on":
        led.on()
        elif toggle == "off":
            led.off()
                else:
                prnt("Try again!")