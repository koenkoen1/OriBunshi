import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import copy
import csv
import datetime
import math
import random
from amino_acid import Amino_Acid
from molecule import Molecule
from randomturns import randomturns
from greedyfold import spiralfold

BEGINTEMP = 200


def filepath():
    """
    Outputs a filepath for saving output data.
    """

    # save output in results directory
    path = "./results/"

    # increment filename with 1 wrt last file, to not overwrite it
    i = 0
    while os.path.exists(f"{path}annealing{i}.csv"):
        i += 1

    filepath = f"{path}annealing{i}.csv"

    return filepath


def tempfunc(k):
    return  (BEGINTEMP / (1 + math.log10(1 + k)))


def kfunc(temp):
    return 10 ** (BEGINTEMP/temp - 1) - 1


def write_csv(outfile, data, molecule):
    """
    Output a CSV file with given data.
    """
    writer = csv.writer(outfile)

    # write header
    writer.writerow([datetime.datetime.now(),])
    writer.writerow([f'sequence = {molecule.sequence}',])
    writer.writerow([f'start temperature = {BEGINTEMP}',])
    writer.writerow(['temperature', 'stability'])

    # iterate over and write movies
    for iteration in data:
        writer.writerow(iteration)


def anneal(molecule, save_data=False):
    spiralfold(molecule, len(molecule.sequence))
    k = 0
    temperature = tempfunc(k)
    reheat = 0
    data = []

    while reheat < 2:
        k += 1
        # print(f"Temp: {temperature}")
        currentstability = molecule.stability()
        # print(f"stability: {currentstability}")

        save_iter = [temperature, currentstability]
        data.append(save_iter)

        oldmolecule = copy.deepcopy(molecule)
        randomturns(molecule, random.randint(0, 3))

        molecule.force_vadil()

        if molecule.stability() < currentstability:
            temperature = tempfunc(k)
        else:
            temperature = tempfunc(k)
            acceptprobability = math.exp(((currentstability -
                                           molecule.stability()) * 175)
                                         / temperature)
            x = random.uniform(0,1)
            if acceptprobability < x:
                molecule = oldmolecule
        if temperature < 37:
            k = kfunc(50)
            reheat += 1

    if save_data:
        with open(filepath(), 'w', newline='') as output_file:
            write_csv(output_file, data, molecule)

    return molecule
