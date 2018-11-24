import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
import math
import random
from amino_acid import Amino_Acid
from molecule import Molecule
from randomturns import randomturns
from greedyfold import spiralfold


def aneal(molecule):
    temperature = 200

    while temperature > 0.1:

        print(f"Temp: {temperature}")
        print(f"stability: {molecule.stability()}")
        currentstability = molecule.stability()
        oldmolecule = copy.deepcopy(molecule)
        randomturns(molecule, random.randint(0, 3))

        if not molecule.check_vadility():
             molecule = oldmolecule
        elif molecule.stability() < currentstability:
            temperature *= 0.999
        else:
            temperature *= 0.999
            acceptprobability = math.exp(((currentstability -
                                           molecule.stability()) * 80)
                                         / temperature)
            print(acceptprobability)
            x = random.uniform(0,1)
            
            if acceptprobability < x:
                molecule = oldmolecule

    return molecule


if __name__ == '__main__':
    molecule = Molecule('HHPHHHPH', 'direct')
    molecule = aneal(molecule)
    print(molecule.check_vadility())
    molecule.draw()
