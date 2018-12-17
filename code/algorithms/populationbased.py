# 2018-12-06 02:53:12.483872
# 2018-12-05 23:40:23.967193

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
from hillclimb import hillclimb
from operator import itemgetter

HILLCLIMBITER = 10


def populationbased(sequence, popsize, gen, save_data=False):
    """
    Population based algorithmself.
    Usage: (sequence, populationsize, generationsize)
    """
    # prints the current time
    print(datetime.datetime.now())

    # Produce a variable to keep track of the amount of stability calls
    call = 0

    # Make a data holder for the write_csv and empty population
    data = []
    pop = []

    # make the population and calculate their stability
    for i in range(popsize):
        molecule = Molecule(sequence, "random")
        pop.append([molecule, 0])

    # variable to keep track of the iterations
    iterations = 0

    # while stopcondition is not reached (amount of generations made)
    while iterations < gen:

        # list for new population
        newpop = []

        # get all the molecules
        list = [list[0] for list in pop]

        #  for every molecule
        for molecule in list:

            # hillclimb twice so two different molecules are made
            molecule1 = hillclimb(molecule, HILLCLIMBITER)
            molecule2 = hillclimb(molecule, HILLCLIMBITER)

            # stability was called in hillclimb
            call += HILLCLIMBITER * 2

            # append the molecules to the new population
            newpop.append([molecule1, molecule1.stability()])
            newpop.append([molecule2, molecule2.stability()])

            # stability was called
            call += 2

        # overwrite the old population
        pop = newpop

        # sort the population based on the stability of the population
        pop = sorted(pop, key=itemgetter(1))

        # eliminate the lower half of the population
        pop = pop[:int(len(pop)/2)]

        # save all the stabilities and average them for results
        datalist = [item[1] for item in pop]
        data.append([call, sum(datalist) / len(datalist)])

        # increase the iterations because this is the end of a generation
        iterations += 1

    # print end time
    print(datetime.datetime.now())

    # save the data in a csv if need be
    if save_data:
        header = ['function evaluations', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}',
                  f'population size = {popsize}',
                  f'generations = {gen}']

        write_csv("population", header, data)

    # return the best molecule found
    return pop[0][0]
