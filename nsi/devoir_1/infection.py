def infection(R0, nb_malades):
    nb_infectes = R0 * nb_malades
    return nb_infectes


print(infection(1.2, 5000))
