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
    solutions = [0 for i in range(len(sequence))]
    molecule = Molecule(sequence[0], 'direct')
    stack.append(molecule)
    lowest = 0
    lowestmolecule = Molecule("H", "direct")
    while stack != []:

        current = stack.pop()
        if len(current.sequence) == len(sequence):
            solutions[int(-current.stability())] += 1
            if lowest > current.stability():
                lowest = current.stability()
                lowestmolecule = copy.deepcopy(current)
        else:
            children(current, sequence)
    print(solutions)
    lowestmolecule.draw()
def children(molecule, sequence):
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
            acid = Amino_Acid(sequence[len(molecule.acids)], (x, y))
            if molecule.add_acids([acid]):
                stack.append(copy.deepcopy(molecule))
                molecule.remove_acids([acid])




if __name__ == '__main__':
    depth("HHPHHHPHPHHHPH")
