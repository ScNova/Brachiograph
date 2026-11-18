from traducteur_servo import traduit
from machine import PWM, Pin
from time import sleep

# Angles du stylo
ANGLE_STYLO_HAUT = 0
ANGLE_STYLO_BAS = 30

# Décalages de calibration
OFFSET_EPAULE = 0.0
OFFSET_COUDE = 0.0

PAUSE_DEPLACEMENT_S = 0.2  # temps laissé aux servos après un G1 A MODIFIER
PAUSE_STYLO_S = 0.3         # temps laissé au poignet après M3 / M5 A MODIFIER

def creer_servo(pin):
    """Crée un servo sur la broche indiquée. (PWM à 50 Hz)."""
    servo = PWM(Pin(pin))
    servo.freq(50)
    return servo

def positionner (servo, angle):
     """Positionne le servo à l'angle demandé"""
     servo.duty_u16(traduit(angle))


def deplacer(servos, S_valeur = None, E_valeur = None):
    """Déplace le bras robotique selon les angles demandés """
    if S_valeur is not None:
        positionner(servos["epaule"],S_valeur + OFFSET_EPAULE)
    if E_valeur is not None:
        positionner(servos["coude"],E_valeur + OFFSET_COUDE)
    sleep(PAUSE_DEPLACEMENT_S)


def desactiver(servos):
    """Désactive les signaux PWM des servomoteurs"""
    for servo in servos.values():
        servo.deinit()
    

def relever_stylo(servo):
    """Relève le stylo"""
    servo.duty_u16(traduit(ANGLE_STYLO_HAUT))
    sleep(PAUSE_STYLO_S)
    

def abaisser_stylo(servo):
    """Abaisse le stylo"""
    servo.duty_u16(traduit(ANGLE_STYLO_BAS))
    sleep(PAUSE_STYLO_S)