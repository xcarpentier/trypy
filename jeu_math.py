def add(n1, n2):
    question = n1, "+", n2, "="
    answer = input.join(question)
    if answer == n1 + n2:
        print("Juste")
    else:
        Faux = "Faux. La réponse est ", n1 + n2
        print.join(Faux)

def sous(n1,n2):
    question = n1, "-", n2, "="
    answer = input.join(question)
    if answer == n1-n2:
        print("Juste")
    else:
        ="Faux. La réponse est ", n1-n2
        print.join(Faux)