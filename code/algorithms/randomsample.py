import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
import math
from amino_acid import Amino_Acid
from molecule import Molecule

def randomsample(sequence, iterations):

        # produces a hardcoded stability list
        solutions = [0 for i in range(len(sequence))]

        i = 0
        while i < iterations:
            molecule = Molecule(sequence, 'random')
            solutions[-molecule.stability()] += 1
            print(i)
            i += 1
        i = 0
        for solution in solutions:
            print(f"-{i}: {solutions[i]}")
            i += 1

if __name__ == '__main__':
    randomsample("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", 100000)