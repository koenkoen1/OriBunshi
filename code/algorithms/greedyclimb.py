import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
from molecule import Molecule

directions = ["Left", "Right"]

def climb(molecule):
    # trying out single turns
    if not turn(1, molecule):
        # trying out double turns
        turn(2, molecule)
    return molecule

def turn(turns, molecule):
    length = len(molecule.sequence)
    route = False
    currentstability = molecule.stability()
    for i in range(1, length - 1):
        for j in range(2):
            for turn in range(turns):
                molecule.turn(i + turn, directions[j])
            if (molecule.check_vadility() and
                molecule.stability() < currentstability):
                currentstability = molecule.stability()
                route = [i, directions[j]]
                molecule.draw()
            for turn in range(turns):
                    molecule.turn(i + turn, directions[j - 1])

    if route:
        molecule.turn(route[0], route[1])
        molecule.turn(route[0] + 1, route[1])
        climb(molecule)
        return True
    return False

if __name__ == '__main__':
    molecule = Molecule('PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP', 'direct')
    mol = climb(molecule)
    mol.draw()
