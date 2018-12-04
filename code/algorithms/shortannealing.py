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

BEGINTEMP = 200

# function that tranforms amount of iterations to a temperature
def tempfunc(k):
    return  (BEGINTEMP / (1 + math.log10(1 + k)))

# function that transforms temperature to iterations
def kfunc(temp):
    return 10 ** (BEGINTEMP/temp - 1) - 1

# function that copies the coordinates from another molecule
def copylocations(molecule1, molecule2):
    for index, amino_acid in enumerate(molecule2.acids):
        molecule1.acids[index].coordinates = amino_acid.coordinates


def shortanneal(molecule, save_data=False):
    loweststability = 1
    lowestmolecule = copy.deepcopy(molecule)
    oldmolecule = copy.deepcopy(molecule)
    k = 0
    temperature = tempfunc(k)
    data = []
    while temperature < 60:
        k += 1
        oldstability = molecule.stability()

        save_iter = [temperature, oldstability]
        data.append(save_iter)

        copylocations(oldmolecule, molecule)
        randomturns(molecule, random.randint(1, 3))

        while not molecule.check_vadility():
            copylocations(molecule, oldmolecule)
            randomturns(molecule, random.randint(1, 3))
        currentstability = molecule.stability()

        if molecule.stability() < oldstability:
            temperature = tempfunc(k)
            if molecule.stability() < loweststability:
                lowestmolecule = copy.deepcopy(molecule)
                loweststability = currentstability
        else:
            temperature = tempfunc(k)
            copylocations(molecule, oldmolecule)

    # write data to csv file if save option was chosen
    if save_data:
        header = ['temperature', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}',
                  f'start temperature = {BEGINTEMP}']

        write_csv("annealing", header, data)

    return lowestmolecule

if __name__ == '__main__':
    molecule = shortanneal(Molecule("HHPHHPHP", "direct"))
    molecule.draw()
