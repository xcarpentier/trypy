import sqlite3

baseDonn = sqlite3.connect("villes.sqlite")
cur = baseDonn.cursor()
while 1:
    requete = input("Veuillez entrer votre requête SQL (ou <Enter> pour terminer) :")
    if requete == "":
        break
    try:
        cur.execute(requete)
    except:
        print("*** Requête SQL incorrecte ***")
    else:
        for enreg in cur:
            print(enreg)
    print()

baseDonn.close()
