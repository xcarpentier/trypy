def danger(R0):
    if R0 < 1:
        contagiosite = "Cette maladie est peu contagieuse."
    elif R0 < 1.5:
        contagiosite = "Cette maladie est assez contagieuse."
    elif R0 < 3:
        contagiosite = "Cette maladie est sérieusement contagieuse."
    elif R0 > 3:
        contagiosite = "Cette maladie est très contagieuse."
    print(contagiosite)
