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



# function that copies the coordinates from another molecule
def copylocations(molecule1, molecule2):
    for index, amino_acid in enumerate(molecule2.acids):
        molecule1.acids[index].coordinates = amino_acid.coordinates

# non determinstic hilclimber algorithm
def hillclimb(molecule, save_data=False):

    # make an molecule and counter for lowest stability
    loweststability = 1
    oldmolecule = copy.deepcopy(molecule)
    k = 0
    data = []

    # if this bool is false at the end it means no better molecule was found
    lowestmolecule = False
    while k < 10:
        k += 1

        # save the molecule state
        oldstability = molecule.stability()
        save_iter = [k, oldstability]
        data.append(save_iter)
        copylocations(oldmolecule, molecule)

        # apply random turns to the molecule (1 to 3 turns)
        randomturns(molecule, random.randint(1, 3))

        # if the molecule is not valid try again
        while not molecule.check_vadility():
            copylocations(molecule, oldmolecule)
            randomturns(molecule, random.randint(1, 3))

        # get the new stability
        currentstability = molecule.stability()

        # if its lower accept it
        if molecule.stability() <= oldstability:
            if molecule.stability() < loweststability:
                lowestmolecule = copy.deepcopy(molecule)
                loweststability = currentstability

        # return to the beginning state
        else:
            copylocations(molecule, oldmolecule)

    # write data to csv file if save option was chosen
    if save_data:
        header = ['temperature', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}']

        write_csv("Hillclimb", header, data)

    # if a lower molecule was found return that else return the molecule
    if lowestmolecule:
        return lowestmolecule
    else:
        return molecule

if __name__ == '__main__':
    molecule = shortanneal(Molecule("HHPHHPHP", "direct"))
    molecule.draw()
