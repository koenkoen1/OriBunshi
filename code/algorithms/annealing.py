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
    return  (BEGINTEMP / (1 + math.log10(1 + k)))


def kfunc(temp):
    return 10 ** (BEGINTEMP/temp - 1) - 1


def copylocations(molecule1, molecule2):
    for index, amino_acid in enumerate(molecule2.acids):
        molecule1.acids[index].coordinates = amino_acid.coordinates



def anneal(molecule, save_data=False):
    loweststability = 1
    lowestmolecule = Molecule('H', 'direct')
    oldmolecule = copy.deepcopy(molecule)
    spiralfold(molecule, len(molecule.sequence))
    k = 0
    temperature = tempfunc(k)
    reheat = 0
    data = []
    maxreheat = 4
    while reheat < maxreheat:
        k += 1
        print(f"Temp: {temperature}")
        currentstability = molecule.stability()
        print(f"stability: {currentstability}")

        save_iter = [temperature, currentstability]
        data.append(save_iter)

        copylocations(oldmolecule, molecule)
        randomturns(molecule, random.randint(1, 2))
        molecule.force_vadil()

        if molecule.stability() < currentstability:
            temperature = tempfunc(k)
            if molecule.stability() < loweststability:
                lowestmolecule = copy.deepcopy(molecule)
        else:
            temperature = tempfunc(k)
            acceptprobability = math.exp(((currentstability -
                                           molecule.stability()) * 175)
                                         / temperature)
            x = random.uniform(0,1)
            if acceptprobability < x:
                copylocations(molecule, oldmolecule)
        if temperature < 40:
            k = kfunc(50)
            reheat += 1

    if save_data:
        header = ['temperature', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}',
                  f'start temperature = {BEGINTEMP}']

        write_csv("annealing", header, data)
    lowestmolecule.draw()

    return lowestmolecule
