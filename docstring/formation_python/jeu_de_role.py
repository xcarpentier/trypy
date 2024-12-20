from random import randint

user_lives = 50
enemy_lives = 50
potion_number = 2
pass_your_turn = False

print("***Jeu de rôles***")

while user_lives and enemy_lives:
    if not pass_your_turn:
        user_choice = input(
            """Choisissez une action :
1. Attaquer l'ennemi.
2. Prendre une potion.
L'action que vous choisissez : """
        )
        if user_choice == "1":
            attack = randint(5, 10)
            enemy_lives -= attack
            print(
                f"Vous avez attaqué l'ennemi et lui avez infligé une perte de {attack} points de vie."
            )
            if enemy_lives <= 0:
                break
        elif user_choice == "2":
            if potion_number > 0:
                potion = randint(15, 50)
                user_lives += potion
                potion_number -= 1
                print(
                    f"Vous avez pris une potion et gagné {potion} points de vie. Il {'vous reste ' if potion_number > 0 else 'ne vous reste aucune'}{potion_number if potion_number > 0 else ''} potion{'s' if potion_number > 1 else ''}."
                )
                pass_your_turn = True
            else:
                print("Vous n'avez plus de potions.")
                print("-" * 65)
                continue
        else:
            print("Cette commande n'existe pas.")
            print("-" * 65)
            continue
    elif pass_your_turn:
        print("Vous passez votre tour...")
        pass_your_turn = False
    attack = randint(5, 15)
    user_lives -= attack
    print(
        f"L'ennemi vous a attaqué et vous a infligé une perte de {attack} points de vie."
    )
    if user_lives <= 0:
        break
    print(
        f"""Vous avez encore {user_lives} points de vie.
Votre ennemi a encore {enemy_lives} points de vie."""
    )
    print("-" * 65)

if user_lives < 1:
    print("Votre ennemi a gagné.")
elif enemy_lives < 1:
    print("Vous avez gagné.")
