def mortalite(nb_habitants):
    hab_restants = nb_habitants * 0.95
    return hab_restants


population = 150000
population_reste = population
semaines = 0

while population_reste > population / 2:
    population_reste = mortalite(population_reste)
    semaines += 1

print(semaines)
