import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))


import copy
from amino_acid import Amino_Acid
from molecule import Molecule

stack = []


def depth(sequence):
    """
    Explores all possible configurations of the molecule by using a Depth first
    algorithm

    Pruning: if a child molecule is found which isn't valid the child is removed
    prints the whole solution space when its done
    """
    # produces a hardcoded stability list
    solutions = [0 for i in range(len(sequence))]

    # produces the first amino acid of the molecule as the molecule
    molecule = Molecule(sequence[0] + sequence[1], 'direct')

    # append this molecule to the stack
    stack.append(molecule)

    # define the lowest stability found (placeholder = 0) + placeholder molecule
    lowest = 1
    lowestmolecule = Molecule("H", "direct")
    while stack != []:
        current = stack.pop()

        # if the length of the sequence equals the input sequence dont make children
        if len(current.sequence) == len(sequence):
            solutions[int(-current.stability())] += 1
            if lowest > current.stability():
                lowest = current.stability()
                lowestmolecule = copy.deepcopy(current)
        else:
            children(current, sequence)

    # draws the solution space
    i = 0
    for stability in solutions:
        print(f"stabilty: {i}: {stability}")
        i -= 1

    # draws the first solution molecule found with the lowest stability
    lowestmolecule.draw()

    # returns this molecule for further usage
    return lowestmolecule


def children(molecule, sequence):
    """
    Produces children of the given molecule by adding an amino acid in every
    possible location and appends this to the stack
    """

    # every direction
    for direction in range(4):
        x, y  = molecule.acids[len(molecule.acids) - 1].coordinates
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        # don't go to y - 1 from straight molecule, to elemininate mirror images
        elif direction == 2 and not straight(molecule):
            y -= 1
        elif direction == 3:
            x -= 1

        # make a new amino acid
        acid = Amino_Acid(sequence[len(molecule.acids)], (x, y))

        # if adding the acid was succesfull
        if molecule.add_acids([acid]):
            stack.append(copy.deepcopy(molecule))
            molecule.remove_acids([acid])


def straight(molecule):
    """
    Checks if molecule is straight (to right from origin). Returns True if this
    is the case, else False.
    """

    for acid in molecule.acids:
        if not acid.coordinates[1] == 0:
            return False
    return True
