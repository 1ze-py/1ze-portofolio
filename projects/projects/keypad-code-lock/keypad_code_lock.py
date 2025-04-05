import RPi.GPIO as GPIO
import time

# broches 3x4
LIGNES = [7, 8, 11, 25]  # lignes clavier
COLONNES = [9, 10, 15]   # colonnes clavier

# Mapping des touches 
TOUCHES = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

CODE_SECRET = "1234"

def initialiser_gpio():
    GPIO.setmode(GPIO.BCM)
    for ligne in LIGNES:
        GPIO.setup(ligne, GPIO.OUT)
        GPIO.output(ligne, GPIO.LOW)
    for colonne in COLONNES:
        GPIO.setup(colonne, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def lire_clavier():
    for i, ligne in enumerate(LIGNES):
        GPIO.output(ligne, GPIO.HIGH)
        for j, colonne in enumerate(COLONNES):
            if GPIO.input(colonne) == GPIO.HIGH:
                GPIO.output(ligne, GPIO.LOW)
                return TOUCHES[i][j]
        GPIO.output(ligne, GPIO.LOW)
    return None

def verifier_code():
    saisie = ""
    print("Veuillez entrer le code :")
    while True:
        touche = lire_clavier()
        if touche:
            print(f"Touche pressée : {touche}")
            if touche == '#':
                if saisie == CODE_SECRET:
                    print("Code correct. Accès autorisé.")
                else:
                    print("Code incorrect. Accès refusé.")
                saisie = ""
            elif touche == '*':
                saisie = ""
                print("Saisie réinitialisée.")
            else:
                saisie += touche
        time.sleep(0.3)

try:
    initialiser_gpio()
    verifier_code()
except KeyboardInterrupt:
    print("\nProgramme interrompu.")
finally:
    GPIO.cleanup()
