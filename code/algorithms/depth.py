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

    Pruning: if a child molecule is found wich isn't valid the child is removed
    prints a list of all solutions in a list [stability = 0, -1 , -2, etc..]
    """
    # produces a hardcoded stability list
    solutions = [0 for i in range(len(sequence))]

    # produces the first amino acid of the molecule as the molecule
    molecule = Molecule(sequence[0], 'direct')

    # append this molecule to the stack
    stack.append(molecule)

    # define the lowest stability found (placeholder = 0) and a placeholder molecule
    lowest = 0
    lowestmolecule = Molecule("H", "direct")
    while stack != []:
        current = stack.pop()

        # if the length of the sequence equals the imput sequence dont make children
        if len(current.sequence) == len(sequence):
            solutions[int(-current.stability())] += 1
            if lowest > current.stability():
                lowest = current.stability()
                lowestmolecule = copy.deepcopy(current)
        else:
            children(current, sequence)

    # draws the solution space
    i = 0
    for stability in solutions
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
            elif direction == 2:
                y -= 1
            else:
                x -= 1

            # make a new amino acid
            acid = Amino_Acid(sequence[len(molecule.acids)], (x, y))

            # if adding the acid was succesfull
            if molecule.add_acids([acid]):
                stack.append(copy.deepcopy(molecule))
                molecule.remove_acids([acid])
