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


<<<<<<< HEAD
def tempfunc(k):
    return  (begintemperature / (1 + math.log10(1 + k)))



def aneal(molecule):
    begintemperature = 200
    k = 0
    temperature = tempfunc(k)
    while temperature > 34:
        k += 1
=======
def aneal(molecule):
    temperature = 200

    while temperature > 0.1:

>>>>>>> d9959ec827dd576183f0cdaae947be9785ba24a3
        print(f"Temp: {temperature}")
        print(f"stability: {molecule.stability()}")
        currentstability = molecule.stability()
        oldmolecule = copy.deepcopy(molecule)
        randomturns(molecule, random.randint(0, 3))

        if not molecule.check_vadility():
             molecule = oldmolecule
             k -= 1
        elif molecule.stability() < currentstability:
            temperature = tempfunc(k)
        else:
<<<<<<< HEAD
            temperature = tempfunc(k)
            acceptprobability = math.exp(((currentstability - molecule.stability()) * 200) / temperature)
=======
            temperature *= 0.999
            acceptprobability = math.exp(((currentstability -
                                           molecule.stability()) * 80)
                                         / temperature)
            print(acceptprobability)
>>>>>>> d9959ec827dd576183f0cdaae947be9785ba24a3
            x = random.uniform(0,1)
            
            if acceptprobability < x:
                molecule = oldmolecule

    return molecule


if __name__ == '__main__':
    molecule = Molecule('HPHPPHHPHPPHPHHPPHPH', 'direct')
    spiralfold(molecule, len(molecule.sequence))
    molecule = aneal(molecule)
    print(molecule.check_vadility())
    molecule.draw()
