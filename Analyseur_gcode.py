
def lire_fichier(nom_fichier):
    """Lit le fichier G-Code et retourne une liste d'instructions"""
    instructions = []
    with open(nom_fichier,"r") as file:
        for line in file:
            elements = line.strip().split() # separe une ligne de fichier en une liste 

            if not elements: # si c'est une ligne vide on passe a la ligne suivante 
                continue

            commande = elements[0] # on conserve la commande dans une variable donc commande = M3

            parametres = {}

            for element in elements[1:]: # loop tout les elements apres l'element de commande retourne un format dictionnaire 
                nom_parametre = element[0]
                valeur = float(element[1:])
                parametres[nom_parametre] = valeur

            instruction = (commande, parametres)
            instructions.append(instruction) # on aura un format (commande,{nom_parametre: valeur_parametre, ...})

    return instructions # [(commande,{nom_parametre: valeur_parametre,...}),...]





