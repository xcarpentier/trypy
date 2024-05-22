from time import sleep
import sys

LISTE_COURSE = []

while True:
    commande = input(
        """Entrer une de ces commandes :
1. Ajouter un élément à la liste.
2. Supprimer un élément de la liste.
3. Supprimer tous les éléments de la liste.
4. Afficher la liste.
5. Quitter.
Entrez votre commande : """
    )
    if commande == "1":
        element = input("Entrer l'élément à ajouter : ")
        LISTE_COURSE.append(element)
        print(f"L'élément {element} a bien été ajouté.")
        sleep(2)
    elif commande == "2":
        element = input("Entrer l'élément à supprimer : ")
        if element in LISTE_COURSE:
            LISTE_COURSE.remove(element)
            print(f"L'élément {element} a bien été supprimé.")
            sleep(2)
        else:
            print(f"Désolé, l'élément {element} n'existe pas.")
            sleep(2)
    elif commande == "3":
        if LISTE_COURSE:
            confirm = input(
                "Êtes-vous sûr de vouloir supprimer tout le contenu de votre liste ? Vous ne pourrez pas revenir en arrière. oui/non : "
            ).lower()
            if confirm == "oui":
                LISTE_COURSE.clear()
                print("Tout le contenu de la liste a bien été supprimé.")
                sleep(2)
            elif confirm != "non":
                print(f"Désolé, je ne comprend pas cette réponse : {confirm}")
                sleep(2)
        else:
            print("Votre liste est vide. Il n'y a rien à supprimer.")
            sleep(2)
    elif commande == "4":
        if LISTE_COURSE:
            print("Voici votre liste :")
            i = 1
            for element in LISTE_COURSE:
                print(f"{i}. {element}")
                i += 1
            sleep(len(LISTE_COURSE) * 1 + 1)
        else:
            print("Votre liste est vide. Il n'y a rien à afficher.")
            sleep(2)
    elif commande == "5":
        print("Au revoir !")
        sleep(1)
        sys.exit()
    else:
        print("Désolé cette commande est inconnue.")
        sleep(2)
    print("-" * 50)
