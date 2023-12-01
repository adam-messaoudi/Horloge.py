import time

heure_actuelle = (0, 0, 0)
alarme = None
mode_affichage = "24"

def afficher_heure(heure):
    global heure_actuelle
    heure_actuelle = heure
    
    heures = heure[0] % 12 if mode_affichage == "12" else heure[0] if heure[0] >= 12 else heure[0] + 12
    affixe = "AM" if mode_affichage == "12" else "PM"
    
    print(f"{heures:02d}:{heure[1]:02d}:{heure[2]:02d} {affixe}")

def regulager_heure(nouvelle_heure):
    afficher_heure(nouvelle_heure)

def regulager_alarme(nouvelle_alarme):
    global alarme
    alarme = nouvelle_alarme

def verifier_alarme():
    global alarme
    if alarme is not None and heure_actuelle == alarme:
        print("L'alarme a sonné !")

def choisir_mode_affichage(nouveau_mode):
    global mode_affichage
    mode_affichage = nouveau_mode

def demander_mode_affichage():
    while True:
        mode = input("Veuillez choisir un mode d'affichage de l'heure (12 ou 24) : ")
        if mode in ["12", "24"]:
            choisir_mode_affichage(mode)
            break
        else:
            print("Mode d'affichage invalide. Veuillez réessayer.")

heures = [(i, j, k) for i in range(24) for j in range(60) for k in range(60)]

demander_mode_affichage()
regulager_alarme((0, 0, 5))

while True:
    for heure in heures:
        regulager_heure(heure)
        verifier_alarme()
        time.sleep(1)
