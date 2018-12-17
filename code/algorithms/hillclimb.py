import copy
import datetime
import math
import random
from randomturns import randomturns
from write_csv import write_csv
from copylocations import copylocations

def hillclimb(molecule, iterations, save_data=False):
    """
    Non-determinstic hilclimber algorithm.
    It requires a Molecule object, the amount of iterations that should be
    performed and optionally a boolean to indicate whether the resulting data
    should be saved.
    """

    # make an molecule and counter for lowest stability
    loweststability = 1
    oldmolecule = copy.deepcopy(molecule)
    k = 0
    data = []

    # if this bool is false at the end it means no better molecule was found
    lowestmolecule = False
    while k < iterations:
        k += 1

        # save the molecule state
        oldstability = molecule.stability()
        save_iter = [k, oldstability]
        data.append(save_iter)
        copylocations(oldmolecule, molecule)

        # apply random turns to the molecule (1 to 3 turns)
        randomturns(molecule, random.randint(1, 3))

        # if the molecule is not valid try again
        while not molecule.check_validity():
            copylocations(molecule, oldmolecule)
            randomturns(molecule, random.randint(1, 3))

        # get the new stability
        currentstability = molecule.stability()

        # if its lower accept it
        if molecule.stability() <= oldstability:
            if molecule.stability() < loweststability:
                lowestmolecule = copy.deepcopy(molecule)
                loweststability = currentstability

        # else return to the beginning state
        else:
            copylocations(molecule, oldmolecule)

    # write data to csv file if save option was chosen
    if save_data:
        header = ['temperature', 'stability',
                  datetime.datetime.now(),
                  f'sequence = {molecule.sequence}']

        write_csv("Hillclimb", header, data)

    # if a lower molecule was found return that else return the molecule
    if lowestmolecule:
        return lowestmolecule
    else:
        return molecule
