import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
import datetime
import math
from amino_acid import Amino_Acid
from molecule import Molecule
from write_csv import write_csv


def randomsample(sequence, iterations, save_data=False):

    # produce list with max amount of possible stabilities, to count solutions
    solutions = [[-i, 0] for i in range(len(sequence))]

    for i in range (iterations):
        molecule = Molecule(sequence, 'random')
        solutions[-molecule.stability()][1] += 1

    print(solutions)

    # write data to csv file if save option was chosen
    if save_data:
        header = ['stability', 'solutions found',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}']

        write_csv("randomsample", header, solutions)


if __name__ == '__main__':
    randomsample("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", 100000)
