from Controle_servos import deplacer, desactiver, abaisser_stylo, relever_stylo



def executeur (servos, commande, parametres):
    """Exécute les fonctions de contrôle correspondant à la commande G-Code reçue"""
    if commande == "G1":
        deplacer(servos, parametres.get("S"), parametres.get("E"))
                          
    elif commande == "M3":
        abaisser_stylo(servos["poignet"])
      
    elif commande == "M5":
        relever_stylo(servos["poignet"])
      
    elif commande == "M18":
        desactiver(servos)
        return True

    else:
        print("commande non reconnue: ", commande)

    return False

        

