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
    k = 0
    temperature = tempfunc(k)
    reheat = 0
    data = []
    maxreheat = 8
    while reheat < maxreheat:
        k += 1
        print(f"Temp: {temperature}")
        oldstability = molecule.stability()
        print(f"stability: {oldstability}")

        save_iter = [temperature, oldstability]
        data.append(save_iter)

        copylocations(oldmolecule, molecule)
        randomturns(molecule, random.randint(1, 3))
        molecule.force_vadil()
        currentstability = molecule.stability()

        if molecule.stability() < oldstability:
            temperature = tempfunc(k)
            if molecule.stability() < loweststability:
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
        if temperature < 41:
            k = kfunc(200)
            reheat += 1

    # write data to csv file if save option was chosen
    if save_data:
        header = ['temperature', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}',
                  f'start temperature = {BEGINTEMP}']

        write_csv("annealing", header, data)
    lowestmolecule.draw()

    return lowestmolecule
