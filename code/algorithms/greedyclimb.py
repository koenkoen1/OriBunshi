import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

from molecule import Molecule

directions = ["Left", "Right"]

def climb(molecule):
    """
    A maximum ascent hillclimber algorithm, which takes a molecule object and
    modifies it according to the algorithm.
    """
    # tries out single turns
    if not turn(1, molecule):
        # tries out double turns
        turn(2, molecule)

def turn(turns, molecule):
    """
    A function used by the maximum ascent hillclimber to test all configurations
    that are a certain amount of turns away from the current molecule object.

    It is implemented with recursion, with the stop condition being when no
    turns can improve stability
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
        climb(molecule)
        return True

    return False

if __name__ == '__main__':
    molecule = Molecule('PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP', 'direct')
    climb(molecule)
    molecule.draw()
