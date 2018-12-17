#  Simulated annealing algorithm using reheating
# imput is a molecule, times to reheat, at what temp it should reheat_temp
# returns best molecule found

import copy
import datetime
import math
import random
from randomturns import randomturns
from greedyfold import spiralfold
from write_csv import write_csv
from copylocations import copylocations

# Defines the beginning temperature, should not be adjusted
BEGINTEMP = 200

# math functions
def tempfunc(k):
    """
    Calculates temperature from the amount of iterations.
    This function is used to calculate the next temperature.
    """
    return  (BEGINTEMP / (1 + math.log10(1 + k)))

def kfunc(temp):
    """
    Calculates what the amount of iterations would be at a certain temperature.
    This function is used for reheating.
    """
    return 10 ** (BEGINTEMP/temp - 1) - 1

def anneal(molecule, reheat_times, reheat_temp, save_data=False):
    """
    A simulated annealing algorithm.
    It requires a Molecule object, reheating times, reheat temperature and optionally a boolean to indicate whether
    the resulting data should be saved.
    """
    # produce two molecules identical to the original molecule
    lowestmolecule = copy.deepcopy(molecule)
    oldmolecule = copy.deepcopy(molecule)

    # placeholder for lowest stability (stability cannot be higher than 0 so
    # this will always be overwritten in the first iteration)
    loweststability = 1

    # calculate the current stability
    currentstability = molecule.stability()

    # iteration, reheat and function-call counters
    k = 0
    reheat = 0
    call = 1

    # temperature variable
    temperature = tempfunc(k)

    # data list for write_csv
    data = []

    # main loop that keeps track of end condition (all reheating has been done)
    while reheat < reheat_times:

        # increase iterations
        k += 1

        # copy information about the molecule that is to be altered
        oldstability = currentstability
        copylocations(oldmolecule, molecule)

        #  save the current data about the algorithm
        save_iter = [temperature, call, oldstability]
        data.append(save_iter)

        # make some random turns which are forced to be valid
        randomturns(molecule, random.randint(1, 3))
        molecule.force_valid()

        # update the current stability
        currentstability = molecule.stability()
        call += 1

        # if this stability is better than the old stability accept the change
        if currentstability <= oldstability:

            # if its better than the best stability save the molecule
            if currentstability < loweststability:
                lowestmolecule = copy.deepcopy(molecule)
                loweststability = currentstability

        # if the stability is worse than the old stability
        else:

            # calculate the chance to accept the new molecule
            acceptprobability = math.exp(((oldstability -
                                           currentstability) * 170)
                                         / temperature)
            x = random.uniform(0,1)

            # if not accepted, return to previous configuration
            if acceptprobability < x:
                copylocations(molecule, oldmolecule)
                currentstability = oldstability

        # update the temperature
        temperature = tempfunc(k)

        # if the temperature is below the reheat temperature reheat the system
        if temperature < reheat_temp:
            k = kfunc(200)
            reheat += 1

            # prints a variable to keep track of the progress
            print(reheat)

    # write data to csv file if save option was chosen
    if save_data:
        header = ['temperature', 'function evaluations', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}',
                  f'start temperature = {BEGINTEMP}',
                  f'reheat_times = {reheat_times}',
                  f'reheat_temp = {reheat_temp}']

        write_csv("annealing", header, data)

    # return the lowest molecule
    return lowestmolecule
