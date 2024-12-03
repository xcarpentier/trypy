from random import randint
from time import sleep
from datetime import datetime


def min_max_choice(inter_mini: int):
    while True:
        while True:
            mini = input("Choisis un nombre minimum : ")
            try:
                mini = int(mini)
                break
            except ValueError:
                print("Ce que vous avez entré pour nombre minimum n'est pas un nombre.")
                sleep(1.5)

        while True:
            maxi = input("Choisis un nombre maximum : ")
            try:
                maxi = int(maxi)
                break
            except ValueError:
                print("Ce que vous avez entré pour nombre maximum n'est pas un nombre.")
                sleep(1.5)

        if mini > maxi:
            print("Votre nombre minimum est plus grand que votre nombre maximum.")
            sleep(1.5)
        elif maxi - mini + 1 < inter_mini:
            print(
                f"L'intervale entre votre nombre minimum et votre nombre maximum est inférieur à {inter_mini}."
            )
            sleep(1.5)
        else:
            break
    print("-" * 40)
    return mini, maxi


def def_a_b(mini: int, maxi: int):
    a = randint(mini, maxi)
    b = randint(mini, maxi)
    return a, b


def number(user_response):
    try:
        user_response = int(user_response)
        return user_response
    except ValueError:
        print("Ce que vous avez entré comme réponse n'est pas un nombre.")
        sleep(1.5)


def correct(
    user_response, c: int, score: int, square: bool = False, division: bool = False
):
    if not square and not division:
        if user_response == c:
            print(f"✓ Bravo, la réponse était bien {c}.")
            sleep(1.5)
            score += 1
        else:
            print(f"✗ Dommage, la réponse était {c}.")
            sleep(1.5)
    elif square:
        if user_response == c or user_response == -c:
            if c != 0:
                print(f"✓ Bravo, la réponse était bien {c} ou {-c}.")
            else:
                print(f"✓ Bravo, la réponse était bien {c}.")
            sleep(1.5)
            score += 1
        else:
            print(f"✗ Dommage, la réponse était {c} ou {-c}.")
            sleep(1.5)
    elif division:
        if calculation != "0/0":
            if user_response == c:
                print(f"✓ Bravo, la réponse était bien {c}.")
                sleep(1.5)
                score += 1
            else:
                print(f"✗ Dommage, la réponse était {c}.")
                sleep(1.5)
        else:
            print("✓ Bonne réponse. En effet toutes les réponses sont bonnes pour 0/0.")
    return score


total_score = 0


while True:
    calculation_list = []
    score = 0

    print("***Math game***")
    sleep(1)

    user_choice = input(
        """1. Additions
2. Soustractions
3. Multiplications
4. Divisions
5. Carrés
6. Racines carrées
7. Cubes
8. Racines cubiques
9. Quitter
Choisis une commande : """
    )
    print("-" * 40)

    if user_choice == "1":
        print("*Additions*")
        sleep(1)
        mini, maxi = min_max_choice(inter_mini=10)

        start_time = datetime.timestamp(datetime.now())
        for question_number in range(1, 11):
            while True:
                a, b = def_a_b(mini=mini, maxi=maxi)
                c = a + b
                calculation = f"{a}+{f'({b})' if b < 0 else b}"
                if not calculation in calculation_list:
                    break

            print(f"Question {question_number}/10")
            sleep(0.5)
            calculation_list.append(calculation)
            user_response = input(calculation + "=")
            user_response = number(user_response=user_response)
            score = correct(user_response=user_response, c=c, score=score)
            print("-" * 40)
        stop_time = datetime.timestamp(datetime.now())

    elif user_choice == "2":
        print("*Soustractions*")
        sleep(1)
        mini, maxi = min_max_choice(inter_mini=10)

        start_time = datetime.timestamp(datetime.now())
        for question_number in range(1, 11):
            while True:
                a, b = def_a_b(mini=mini, maxi=maxi)
                c = a - b
                calculation = f"{a}-{f'({b})' if b < 0 else b}"
                if not calculation in calculation_list:
                    break

            print(f"Question {question_number}/10")
            sleep(0.5)
            calculation_list.append(calculation)
            user_response = input(calculation + "=")
            user_response = number(user_response=user_response)
            score = correct(user_response=user_response, c=c, score=score)
            print("-" * 40)
        stop_time = datetime.timestamp(datetime.now())

    elif user_choice == "3":
        print("*Multiplications*")
        sleep(1)
        mini, maxi = min_max_choice(inter_mini=10)

        start_time = datetime.timestamp(datetime.now())
        for question_number in range(1, 11):
            while True:
                a, b = def_a_b(mini=mini, maxi=maxi)
                c = a * b
                calculation = f"{a}*{f'({b})' if b < 0 else b}"
                if not calculation in calculation_list:
                    break

            print(f"Question {question_number}/10")
            sleep(0.5)
            calculation_list.append(calculation)
            user_response = input(calculation + "=")
            user_response = number(user_response=user_response)
            score = correct(user_response=user_response, c=c, score=score)
            print("-" * 40)
        stop_time = datetime.timestamp(datetime.now())

    elif user_choice == "4":
        print("*Divisions*")
        sleep(1)
        mini, maxi = min_max_choice(inter_mini=10)

        start_time = datetime.timestamp(datetime.now())
        for question_number in range(1, 11):
            while True:
                c, b = def_a_b(mini=mini, maxi=maxi)
                a = c * b
                calculation = f"{a}/{f'({b})' if b < 0 else b}"
                if not calculation in calculation_list:
                    break

            print(f"Question {question_number}/10")
            sleep(0.5)
            calculation_list.append(calculation)
            user_response = input(calculation + "=")
            user_response = number(user_response=user_response)
            score = correct(
                user_response=user_response, c=c, score=score, division=True
            )
            print("-" * 40)
        stop_time = datetime.timestamp(datetime.now())

    elif user_choice == "5":
        print("*Carrés*")
        sleep(1)
        mini, maxi = min_max_choice(inter_mini=10)

        start_time = datetime.timestamp(datetime.now())
        for question_number in range(1, 11):
            while True:
                a = randint(mini, maxi)
                c = a**2
                if not a in calculation_list:
                    break

            print(f"Question {question_number}/10")
            sleep(0.5)
            calculation_list.append(a)
            user_response = input(f"Le carré de {a} est : ")
            user_response = number(user_response=user_response)
            score = correct(user_response=user_response, c=c, score=score)
            print("-" * 40)
        stop_time = datetime.timestamp(datetime.now())

    elif user_choice == "6":
        print("*Racines carrées*")
        sleep(1)
        mini, maxi = min_max_choice(inter_mini=10)

        start_time = datetime.timestamp(datetime.now())
        for question_number in range(1, 11):
            while True:
                c = randint(mini, maxi)
                a = c**2
                if not a in calculation_list:
                    break

            print(f"Question {question_number}/10")
            sleep(0.5)
            calculation_list.append(a)
            user_response = input(f"La racine carrée de {a} est : ")
            user_response = number(user_response=user_response)
            score = correct(user_response=user_response, c=c, score=score, square=True)
            print("-" * 40)
        stop_time = datetime.timestamp(datetime.now())

    elif user_choice == "7":
        print("*Cubes*")
        sleep(1)
        mini, maxi = min_max_choice(inter_mini=5)

        start_time = datetime.timestamp(datetime.now())
        for question_number in range(1, 6):
            while True:
                a = randint(mini, maxi)
                c = a**3
                if not a in calculation_list:
                    break

            print(f"Question {question_number}/5")
            sleep(0.5)
            calculation_list.append(a)
            user_response = input(f"Le cube de {a} est : ")
            user_response = number(user_response=user_response)
            score = correct(user_response=user_response, c=c, score=score)
            print("-" * 40)
        stop_time = datetime.timestamp(datetime.now())

    elif user_choice == "8":
        print("*Racines cubiques*")
        sleep(1)
        mini, maxi = min_max_choice(inter_mini=5)

        start_time = datetime.timestamp(datetime.now())
        for question_number in range(1, 6):
            while True:
                c = randint(mini, maxi)
                a = c**3
                if not a in calculation_list:
                    break

            print(f"Question {question_number}/5")
            sleep(0.5)
            calculation_list.append(a)
            user_response = input(f"La racine cubique de {a} est : ")
            user_response = number(user_response=user_response)
            score = correct(user_response=user_response, c=c, score=score)
            print("-" * 40)
        stop_time = datetime.timestamp(datetime.now())

    elif user_choice == "9":
        print(
            f"{f'Tu as gagné {total_score}' if total_score > 0 else 'Tu n as pas gagné de points pendant cette session.'}"
        )
        print("Au revoir !")
        sleep(1)
        break

    else:
        print("Cette commande n'existe pas.")
        sleep(1)
        continue

    time = round(float(stop_time) - float(start_time))
    print(
        f"""Ton score est de {score}/{question_number} pour cet exercice.
Tu as réalisé cet exercice en {time} secondes."""
    )
    sleep(1.5)
    total_score += score
    print("-" * 40)
