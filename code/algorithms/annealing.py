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


def tempfunc(k):
    begintemperature = 200
    return  (begintemperature / (1 + math.log10(1 + k)))



def aneal(molecule):
    begintemperature = 200
    k = 0
    temperature = tempfunc(k)
    iterations = 0
    while temperature > 32:
        k += 1
        print(f"Temp: {temperature}")
        print(iterations)
        currentstability = molecule.stability()
        oldmolecule = copy.deepcopy(molecule)
        randomturns(molecule, random.randint(0, 3))

        molecule.force_vadil()

        if molecule.stability() < currentstability:
            temperature = tempfunc(k)
        else:
            temperature = tempfunc(k)
            acceptprobability = math.exp(((currentstability - molecule.stability()) * 200) / temperature)
            x = random.uniform(0,1)
            if acceptprobability < x or molecule.stability() == currentstability:
                molecule = oldmolecule
                iterations += 1
            else:
                iterations = 0
        if iterations > 2000:
            iterations = 0
            k -= 1500

    return molecule


if __name__ == '__main__':
    molecule = Molecule('HPHPPHHPHPPHPHHPPHPH', 'direct')
    spiralfold(molecule, len(molecule.sequence))
    molecule = aneal(molecule)
    print(molecule.check_vadility())
    molecule.draw()
