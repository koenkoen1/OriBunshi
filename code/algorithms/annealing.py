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

BEGINTEMP = 200

def tempfunc(k):
    return  (BEGINTEMP / (1 + math.log10(1 + k)))

def kfunc(temp):
    return 10 ** (BEGINTEMP/temp - 1) - 1


def copylocations(molecule1, molecule2):
    for index, amino_acid in enumerate(molecule2.acids):
        molecule1.acids[index].coordinates = amino_acid.coordinates



def anneal(molecule):
    spiralfold(molecule, len(molecule.sequence))
    k = 0
    temperature = tempfunc(k)
    reheat = 0
    maxreheat = 4
    oldmolecule = copy.deepcopy(molecule)

    while reheat < maxreheat or temperature > 36:
        k += 1
        print(f"Temp: {temperature}")
        currentstability = molecule.stability()
        print(f"stability: {currentstability}")
        copylocations(oldmolecule, molecule)
        randomturns(molecule, random.randint(0, 3))
        molecule.force_vadil()

        if molecule.stability() < currentstability:
            temperature = tempfunc(k)
        else:
            temperature = tempfunc(k)
            acceptprobability = math.exp(((currentstability - molecule.stability()) * 180) / temperature)
            x = random.uniform(0,1)
            if acceptprobability < x:
                copylocations(molecule, oldmolecule)
        if temperature < 40:
            k = kfunc(50)
            reheat += 1

    return molecule
