import datetime
import random
from molecule import Molecule
from write_csv import write_csv
from hillclimb import hillclimb
from operator import itemgetter

HILLCLIMBITER = 10


def populationbased(sequence, popsize, gen, save_data=False):
    """
    Population based algorithmself.
    Usage: (sequence, populationsize, generationsize)
    """
    print(datetime.datetime.now())
    call = 0
    data = []
    pop = []
    maxiterations = gen

    for i in range(popsize):
        molecule = Molecule(sequence, "random")
        pop.append([molecule, molecule.stability()])

    iterations = 0

    while iterations < maxiterations:
        print(iterations)
        newpop = []
        list = [list[0] for list in pop]

        for molecule in list:
            molecule1 = hillclimb(molecule, HILLCLIMBITER)
            molecule2 = hillclimb(molecule, HILLCLIMBITER)
            call += HILLCLIMBITER * 2
            newpop.append([molecule1, molecule1.stability()])
            newpop.append([molecule2, molecule2.stability()])
            call += 2

        pop = newpop
        pop = sorted(pop, key=itemgetter(1))
        pop = pop[:int(len(pop)/2)]
        datalist = [item[1] for item in pop]
        data.append([call, sum(datalist) / len(datalist)])
        iterations += 1

    print(datetime.datetime.now())

    if save_data:
        header = ['function evaluations', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}',
                  f'population size = {popsize}',
                  f'generations = {gen}']

        write_csv("population", header, data)

    return pop[0][0]
