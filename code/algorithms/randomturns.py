import random
import copy

def randomturns(molecule, x):
    """
    Requires the molecule object and a number x for the amount of iterations.
    Calls upon turn method of molecule with random parameters. Replaces the
    acids attribute of the molecule with the best sequence found.
    """
    def copylocations(molecule1, molecule2):
        for index, amino_acid in enumerate(molecule2.acids):
            molecule1.acids[index].coordinates = amino_acid.coordinates
    i = 0
    oldmolecule = copy.deepcopy(molecule)
    # lowest = molecule.stability()
    # lowestsequence = copy.deepcopy(molecule.acids)
    indexes = 1
    while indexes:
        copylocations(oldmolecule, molecule)
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
        indexes = molecule.check_vadility(True);
        if indexes:
            copylocations(molecule, oldmolecule)
