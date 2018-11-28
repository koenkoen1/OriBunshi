import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
from molecule import Molecule

directions = ["Left", "Right"]

def climb(molecule, turnpoint = []):
    # trying out single turns
    if not turn(1, molecule):
        # trying out double turns
        turn(2, molecule)

    """ FIXME: snake path(turnpoints)
    # make snaketurn if there is enough space
    prevturn = 0
    for turnpoint in turnpoints
        if turnpoint - prevturn > 4:
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
def turn(turns, molecule):
    length = len(molecule.sequence)
    route = False
    currentstability = molecule.stability()
    for i in range(1, length - 1):
        for direction in directions:
            testmolecule = copy.deepcopy(molecule)
            for turn in range(turns):
                testmolecule.turn(i + turn, direction)
            if (testmolecule.check_vadility() and
                testmolecule.stability() < currentstability):
                currentstability = testmolecule.stability()
                route = [i, direction]
    if route:
        molecule.turn(route[0], route[1])
        molecule.turn(route[0] + 1, route[1])
        molecule.draw()
        climb(molecule, route[0])
        return True
    return False

if __name__ == '__main__':
    molecule = Molecule('PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP', 'direct')
    climb(molecule)
