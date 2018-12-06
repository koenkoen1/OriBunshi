import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

from molecule import Molecule

directions = ["Left", "Right"]

def climb(molecule):
    """
    A maximum ascent hillclimber algorithm.

    Takes a molecule object and checks all solutions with a distance of one
    turn. Then checks all solutions with a distance of two turns. If a better
    solution is found, the molecule is updated. Stops when no changes are made
    to the molecule.
    """

    while turn(1, molecule) or turn(2, molecule):
        continue

def turn(turns, molecule):
    """
    Tests all configurations a certain amount of turns away from current object.
    """
    length = len(molecule.sequence)
    route = False
    currentstability = molecule.stability()

    # iterates over every amino_acid object except the first and last
    for i in range(1, length - 1):
        # tries turning in both directions
        for j in range(2):
            # makes specified amount of turns
            for turn in range(turns):
                molecule.turn(i + turn, directions[j])

            # checks if new configuration is an improvement, record it if it is
            if (molecule.check_vadility() and
                molecule.stability() < currentstability):
                currentstability = molecule.stability()
                route = [i, directions[j]]

            # undoes turning
            for turn in range(turns):
                    molecule.turn(i + turn, directions[j - 1])

    # permanently applies best configuration on the molecule
    if route:
        molecule.turn(route[0], route[1])
        molecule.turn(route[0] + 1, route[1])
        return True

    return False

if __name__ == '__main__':
    molecule = Molecule('PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP', 'direct')
    climb(molecule)
    molecule.draw()
