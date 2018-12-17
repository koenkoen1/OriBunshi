import random

def randomturns(molecule, x):
    """
    Requires the molecule object and a number x for the amount of iterations.
    Calls upon turn method of molecule with random parameters. Replaces the
    acids attribute of the molecule with the best sequence found.
    """
    i = 0
    while i < x:

        #make a random tuns
        randomnode = random.randint(1, len(molecule.acids) - 1)
        randomdirection = random.randint(0, 1)
        if randomdirection == 0:
            randomdirection = 'Right'
        else:
            randomdirection = 'Left'
        molecule.turn(randomnode, randomdirection)
        i = i + 1
