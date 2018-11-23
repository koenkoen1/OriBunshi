import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
from molecule import Molecule

def climb(molecule):
    directions = ["Left", "Right"]
    length = len(str(molecule).split("\n"))
    currentstability = molecule.stability()
    route = []
    change = False
    for i in range(1, length - 1):
        for direction in directions:
            testmolecule = copy.deepcopy(molecule)
            testmolecule.turn(i, direction)
            testmolecule.turn(i + 1, direction)
            if (testmolecule.check_vadility() and
                testmolecule.stability() < currentstability):
                currentstability = testmolecule.stability()
                route = [i, direction]
                change = True
    if change:
        molecule.turn(route[0], route[1])
        molecule.turn(route[0] + 1, route[1])
        molecule.draw()
        climb(molecule)

if __name__ == '__main__':
    molecule = Molecule('HHHPHHHHPHHHHH', 'direct')
    climb(molecule)
