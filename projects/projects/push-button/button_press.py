import RPi.GPIO as GPIO
import time

# Configuration des broches
bouton_pin = 17

# Configuration initiale de la GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(bouton_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Attendez que le bouton soit pressé...")

    while True:
        if GPIO.input(bouton_pin) == GPIO.LOW:
            print("Bouton pressé!")
            time.sleep(0.2)  # Débouncing pour laissez la lumiere
            while GPIO.input(bouton_pin) == GPIO.LOW:
                time.sleep(0.1)  # Attente du relâchement
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
