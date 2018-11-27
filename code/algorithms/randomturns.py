import random
import copy

def randomturns(molecule, x):
    """
    Requires the molecule object and a number x for the amount of iterations.
    Calls upon turn method of molecule with random parameters. Replaces the
    acids attribute of the molecule with the best sequence found.
    """
    i = 0
    # lowest = molecule.stability()
    # lowestsequence = copy.deepcopy(molecule.acids)
    while i < x:
        backupseqence = copy.deepcopy(molecule.acids)

        #make a random turn
        randomnode = random.randint(1, len(molecule.acids) - 1)
        randomdirection = random.randint(0, 1)
        if randomdirection == 0:
            randomdirection = 'Right'
        else:
            randomdirection = 'Left'
        molecule.turn(randomnode, randomdirection)

        #check if the resulting turn is valid
        # if not molecule.check_vadility():
        #     molecule.acids = backupseqence
        # elif lowest > molecule.stability():
        #     lowest = molecule.stability()
        #     lowestsequence = copy.deepcopy(molecule.acids)
        i = i + 1

    # molecule.acids = lowestsequence
