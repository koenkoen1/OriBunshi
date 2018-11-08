import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))


from molecule import Molecule

import random
import copy
def randomturns(molecule)
    i = 0
    lowest = 1
    while i < 5000000:
        print(i)
        backupmolecule = molecule
        randomnode = random.randint(0, len(molecule.sequence) - 1)
        randomdirection = random.randint(0, 1)
        if randomdirection == 0:
            randomdirection = 'Right'
        else:
            randomdirection = 'Left'
        molecule.turn(randomnode, randomdirection)
        if not molecule.check_vadility():
            molecule = backupmolecule
        elif lowest > molecule.stability():
            print('HOI')
            lowest = molecule.stability()
            lowestmolecule = copy.deepcopy(molecule.sequence)
        i = i + 1
    return molecule
