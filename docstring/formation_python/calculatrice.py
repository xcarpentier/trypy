def add(a: float, b: float) -> float:
    c = a + b
    return c


def sub(a: float, b: float) -> float:
    c = a - b
    return c


def mul(a: float, b: float) -> float:
    c = a * b
    return c


def div(a: float, b: float) -> float:
    c = a / b
    return c


def power(a: float, b: float) -> float:
    c = a**b
    return c


while True:
    response = input(
        "Enter your calculation with spaces between numbers and operators, and replace the comma by a point in the decimal numbers, please. To stop the calculator, enter 'stop' : "
    )
    if response == "stop":
        break
    else:
        calcul_elements = response.split()
        if len(calcul_elements) == 3:
            a = float(calcul_elements[0])
            b = float(calcul_elements[2])
            operator = calcul_elements[1]
            if operator == "+":
                c = add(a=a, b=b)
                print(c)
            elif operator == "-":
                c = sub(a=a, b=b)
                print(c)
            elif operator == "*":
                c = mul(a=a, b=b)
                print(c)
            elif operator == "/":
                c = div(a=a, b=b)
                print(c)
            elif operator == "**":
                c = power(a=a, b=b)
                print(c)
            else:
                print("Sorry, the operator is unknown of that calculator.")
        else:
            print(
                "Sorry, that calculation cannot be resoved by that calculator. Maybe it was not wrote correctly. Please read the instructions before typing your calculation."
            )
