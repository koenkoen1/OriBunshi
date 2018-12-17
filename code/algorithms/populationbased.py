# Population based algorithm, takes in a sequence, generation size and amount of iterations
# returns the best molecule found and is able to save data to a csv

import datetime
from molecule import Molecule
from write_csv import write_csv
from hillclimb import hillclimb
from operator import itemgetter

def populationbased(sequence, popsize, gen, save_data=False):
    """
    Population based algorithmself.
    Usage: (sequence, populationsize, generationsize)
    """
    # constant for hillclimber iterations
    HILLCLIMBITER = 10

    # prints the current time
    print(datetime.datetime.now())

    # Make a data holder for the write_csv
    data = []

    # iteration and function-call counters
    iterations = 0
    call = 0

    # make the population
    pop = []
    for i in range(popsize):
        molecule = Molecule(sequence, "random")
        pop.append([molecule, 0])

    # while stopcondition is not reached (amount of generations made)
    while iterations < gen:

        # list for new population
        newpop = []

        # get all the molecules in generation
        list = [list[0] for list in pop]

        # iterate over every molecule in generation
        for molecule in list:

            #  perform stochastic hillclimber twice
            molecule1 = hillclimb(molecule, HILLCLIMBITER)
            molecule2 = hillclimb(molecule, HILLCLIMBITER)

            # append the created molecules to the new population
            newpop.append([molecule1, molecule1.stability()])
            newpop.append([molecule2, molecule2.stability()])

            # update function-calls
            call += HILLCLIMBITER * 2 + 2

        # new population consists of the best half molecule created
        pop = newpop
        pop = sorted(pop, key=itemgetter(1))
        pop = pop[:int(len(pop)/2)]

        # save all the stabilities and average them for results
        datalist = [item[1] for item in pop]
        data.append([call, sum(datalist) / len(datalist)])

        # increase the iterations
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
