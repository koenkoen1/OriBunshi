import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
import datetime
import math
import random
from amino_acid import Amino_Acid
from molecule import Molecule
from randomturns import randomturns
from greedyfold import spiralfold
from write_csv import write_csv

BEGINTEMP = 200


def tempfunc(k):
    """
    Calculates temperature of simulated annealing algorithm.
    """
    return  (BEGINTEMP / (1 + math.log10(1 + k)))


def kfunc(temp):
    """
    Calculates what the amount of iterations would be at a certain temperature.
    This function is used for reheating.
    """
    return 10 ** (BEGINTEMP/temp - 1) - 1


def copylocations(molecule1, molecule2):
    """
    Copies coordinates of the amino acids of one molecule to another molecule.
    This function is used for resetting the molecule to the backup or for
    updating the backup to a new configuration.
    """
    for index, amino_acid in enumerate(molecule2.acids):
        molecule1.acids[index].coordinates = amino_acid.coordinates


def anneal(molecule, save_data=False):
    """
    A simulated annealing algorithm.
    It requires a Molecule object and optionally a boolean to indicate whether
    the resulting data should be saved.
    """
    call = 1
    loweststability = 1
    lowestmolecule = Molecule('H', 'direct')
    oldmolecule = copy.deepcopy(molecule)
    currentstability = molecule.stability()
    k = 0
    temperature = tempfunc(k)
    reheat = 0
    data = []
    maxreheat = 3
    while reheat < maxreheat:
        k += 1
        oldstability = currentstability
        call += 1

        save_iter = [temperature, call, oldstability]
        data.append(save_iter)

        copylocations(oldmolecule, molecule)
        randomturns(molecule, random.randint(1, 3))
        molecule.force_vadil()
        currentstability = molecule.stability()
        call += 1

        if currentstability < oldstability:
            temperature = tempfunc(k)
            if currentstability < loweststability:
                lowestmolecule = copy.deepcopy(molecule)
                loweststability = currentstability
        else:
            temperature = tempfunc(k)
            acceptprobability = math.exp(((oldstability -
                                           currentstability) * 170)
                                         / temperature)
            x = random.uniform(0,1)
            if acceptprobability < x:
                copylocations(molecule, oldmolecule)
        if temperature < 40:
            k = kfunc(200)
            reheat += 1
            print(reheat)

    # write data to csv file if save option was chosen
    if save_data:
        header = ['temperature', 'function evaluations', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}',
                  f'start temperature = {BEGINTEMP}']

        write_csv("annealing", header, data)

    return lowestmolecule

if __name__ == '__main__':
    anneal(Molecule("HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH", "direct"), True)
