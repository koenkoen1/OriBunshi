# 2018-12-06 02:53:12.483872
# 2018-12-05 23:40:23.967193

import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
import datetime
import math
import random
from amino_acid import Amino_Acid
from molecule import Molecule
from randomturns import randomturns
from greedyfold import spiralfold
from write_csv import write_csv
from hillclimb import hillclimb
from operator import itemgetter
import datetime

def geneteic(sequence):
    print(datetime.datetime.now())
    data = []
    pop = []
    maxiterations = 20
    for i in range(300):
        molecule = Molecule(sequence, "random")
        pop.append([molecule, molecule.stability()])
    iterations = 0
    while iterations < maxiterations:
        print(iterations)
        newpop = []
        list = [list[0] for list in pop]
        for molecule in list:
            molecule1 = hillclimb(molecule)
            molecule2 = hillclimb(molecule)
            newpop.append([molecule1, molecule1.stability()])
            newpop.append([molecule2, molecule2.stability()])
        pop = newpop
        pop = sorted(pop, key=itemgetter(1))
        pop = pop[:int(len(pop)/2)]
        datalist = [item[1] for item in pop]
        data.append([iterations, sum(datalist) / len(datalist)])
        iterations += 1
    print(datetime.datetime.now())
    pop[0][0].draw()
    header = ['temperature', 'stability',
              datetime.datetime.now(),
              f'sequence = {molecule.sequence}']

    write_csv("annealing", header, data)




if __name__ == '__main__':
    geneteic("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH")
