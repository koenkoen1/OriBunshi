import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
from molecule import Molecule

def climb(molecule, turnpoint = 0):
    directions = ["Left", "Right"]
    length = len(str(molecule).split("\n"))
    currentstability = molecule.stability()
    route = []
    change = False

    """
    FIXME: snake path
    if turnpoint > 4:
        testmolecule = copy.deepcopy(molecule)
        for i in range(2):
            testymolecule = copy.deepcopy(testmolecule)
            testymolecule.turn(turnpoint + 1, directions[i])
            testymolecule.turn(turnpoint + 2, directions[i - 1])
            if testymolecule.check_vadility():
                testmolecule = testymolecule
        loop = 3
        while loop < turnpoint:
            for i in range(2):
                testymolecule = copy.deepcopy(testmolecule)
                testymolecule.turn(loop - 3, directions[i])
                testymolecule.turn(loop - 2, directions[i - 1])
                testymolecule.turn(loop - 1, directions[i - 1])
                testymolecule.turn(loop, directions[i])
                testymolecule.draw()
                if (testmolecule.check_vadility() and
                    testmolecule.stability() < currentstability):
                    currentstability = testmolecule.stability()
                    route = [loop]
            loop += 1
    """

    # double turns
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
        climb(molecule, route[0])

if __name__ == '__main__':
    molecule = Molecule('HHPHHHPHPHHHPH', 'direct')
    climb(molecule)
