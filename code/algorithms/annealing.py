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
    temperature = 3000

    while temperature > 1:
        temperature -= 1
        currentstability = molecule.stability()
        oldmolecule = copy.deepcopy(molecule)
        randomturns(molecule, random.randint(0, 3))
        if not molecule.force_vadil():
            print('errorrrrr')
            break
        if molecule.stability() < currentstability:
            continue
        else:
            acceptprobability = math.exp((currentstability - molecule.stability()) / temperature)
            if acceptprobability < random.uniform(0, 1):
                molecule = oldmolecule
        molecule.draw()

if __name__ == '__main__':
    molecule = Molecule('HPHPPPHPHPHP', 'direct')
    spiralfold(molecule, len(molecule.sequence))
    aneal(molecule)
    molecule.draw()
