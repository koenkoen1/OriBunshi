import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
import datetime
from molecule import Molecule
from write_csv import write_csv


def randomsample(input_molecule, iterations, save_data=False):
    """
    Creates Molecule objects based on inputted molecule with a random
    configuration and returns the configuration with the best score.
    It requires a Molecule object, the amount of configurations that should be
    created and optionally a boolean to indicate whether the resulting data
    should be saved.
    """

    # produce list with max amount of possible stabilities, to count solutions
    solutions = [[-i, 0] for i in range(len(input_molecule.sequence))]

    best_solution = copy.deepcopy(input_molecule)

    for i in range (iterations):
        molecule = Molecule(input_molecule.sequence, 'random')
        solutions[-molecule.stability()][1] += 1

        if molecule.stability() < best_solution.stability():
            best_solution = copy.deepcopy(molecule)

    # write data to csv file if save option was chosen
    if save_data:
        header = ['stability',
                  'solutions found',
                  datetime.datetime.now(),
                  f'sequence = {input_molecule.sequence}']

        write_csv("randomsample", header, solutions)

    return best_solution


if __name__ == '__main__':
    randomsample("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", 100000)
