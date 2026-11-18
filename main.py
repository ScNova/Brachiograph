from Analyseur_gcode import lire_fichier
from Controle_servos import creer_servo
from Interpreteur_gcode import executeur

# Nom du fichier G-Code à exécuter
nom_fichier = "circle.gcode"

# Configuration des broches
PIN_EPAULE = 0
PIN_COUDE = 1
PIN_POIGNET = 2

def main():

    # Crée et initialise les signaux PWM associés aux servomoteurs
    servos = {
        "epaule": creer_servo(PIN_EPAULE),
        "coude": creer_servo(PIN_COUDE),
        "poignet": creer_servo(PIN_POIGNET)

        }

    # Lit le fichier G-Code et récupère la liste des instructions 
    instructions = lire_fichier(nom_fichier)

    # Exécute les instructions dans l'ordre du fichier
    for commande, parametres in instructions:
        if executeur(servos, commande, parametres):
            break

if __name__ == "__main__":
    main()