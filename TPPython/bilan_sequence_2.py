import math

a = float(input("Donnez moi un nombre décimal positif:"))
b = float(input("Donnez moi un autre nombre décimal positif:"))
c = float(input("Donnez moi un dernier nombre décimal positif:"))
while min(a, b) + min(min(a, b), c) < max(a, b, c):
    a = float(
        input(
            "Ces valeurs ne correspondent pas au longueurs des côtés d'un triangle. Donnez moi un nombre décimal positif:"
        )
    )
    b = float(input("Donnez moi un autre nombre décimal positif:"))
    c = float(input("Donnez moi un dernier nombre décimal positif:"))
p = (a + b + c) / 2
r = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(
    "L'air du triangle dont les côtés sont a = ",
    a,
    ", b = ",
    b,
    " et c = ",
    c,
    " a pour aire ",
    r,
)
