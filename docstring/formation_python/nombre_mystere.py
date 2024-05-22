from random import randint


NUMBER_TO_FIND = randint(0, 100)
remaining_attempts = 5

print(
    """*** Le nombre mystère ***
Essayez de trouver le nombre mystère qui se situe entre 0 et 100 inclus."""
)

while remaining_attempts > 0:
    print(
        f"Il vous reste {remaining_attempts} tour{'s' if remaining_attempts > 1 else ''}"
    )
    user_choice = input("Choisissez votre nombre : ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 0 <= user_choice <= 100:
            if user_choice < NUMBER_TO_FIND:
                print(
                    f"Le nombre mystère n'est pas {user_choice}. Le nombre mystère est plus grand que {user_choice}."
                )
            elif user_choice > NUMBER_TO_FIND:
                print(
                    f"Le nombre mystère n'est pas {user_choice}. Le nombre mystère est plus petit que {user_choice}."
                )
            else:
                break
            remaining_attempts -= 1
        else:
            print("Votre nombre n'est pas situé entre 0 et 100 inclus.")
    else:
        print("Ce que vous avez entré n'est pas un nombre.")
    print("-" * 65)

if remaining_attempts == 0:
    print(f"Dommage, le nombre mystère est {NUMBER_TO_FIND}.")
elif remaining_attempts > 0:
    tours = 6 - remaining_attempts
    print(
        f"""Bravo, le nombre mystère est bien {NUMBER_TO_FIND}.
Vous avez gagné en {tours} tour{'s' if tours > 1 else ''}."""
    )

print("Fin du jeu.")
