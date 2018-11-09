import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))


from molecule import Molecule

import random
import copy
def randomturns(molecule, x):
    i = 0
    lowest = 1
    while i < x:
        print(i)
        backupmolecule = copy.deepcopy(molecule)
        randomnode = random.randint(0, len(molecule.sequence) - 1)
        randomdirection = random.randint(0, 1)
        if randomdirection == 0:
            randomdirection = 'Right'
        else:
            randomdirection = 'Left'
        molecule.turn(randomnode, randomdirection)
        if not molecule.check_vadility():
            molecule = copy.deepcopy(backupmolecule)
        elif lowest > molecule.stability():
            lowest = molecule.stability()
            lowestmolecule = copy.deepcopy(molecule)
        i = i + 1
    molecule = lowestmolecule
