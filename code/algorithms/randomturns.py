import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import random
import copy


def randomturns(molecule, x):
    i = 0
    lowest = molecule.stability()
    lowestsequence = copy.deepcopy(molecule.sequence)
    print(lowest)
    while i < x:
        print(i)
        backupseqence = copy.deepcopy(molecule.sequence)
        randomnode = random.randint(0, len(molecule.sequence) - 1)
        randomdirection = random.randint(0, 1)
        if randomdirection == 0:
            randomdirection = 'Right'
        else:
            randomdirection = 'Left'
        molecule.turn(randomnode, randomdirection)
        if not molecule.check_vadility():
            molecule.sequence = backupseqence
        elif lowest > molecule.stability():
            print("replacing")
            lowest = molecule.stability()
            lowestsequence = copy.deepcopy(molecule.sequence)
        i = i + 1
    molecule.sequence = lowestsequence
