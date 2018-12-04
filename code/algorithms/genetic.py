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
from shortannealing import shortanneal
from operator import itemgetter

def geneteic(sequence):
    pop = []
    maxiterations = 1000
    for i in range(100):
        molecule = Molecule(sequence, "random")
        pop.append([molecule, molecule.stability()])
    iterations = 0
    while iterations < maxiterations:
        print(iterations)
        newpop = []
        list = [list[0] for list in pop]
        for molecule in list:
            molecule1 = shortanneal(molecule)
            molecule2 = shortanneal(molecule)
            newpop.append([molecule1, molecule1.stability()])
            newpop.append([molecule2, molecule2.stability()])
        pop = newpop
        pop = sorted(pop, key=itemgetter(1))
        pop = pop[:int(len(pop)/2)]
        iterations += 1
    pop[0][0].draw()



if __name__ == '__main__':
    geneteic("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH")
