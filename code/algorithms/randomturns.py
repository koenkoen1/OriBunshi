import random
import copy

def randomturns(molecule, x):
    i = 0
    lowest = molecule.stability()
    lowestsequence = copy.deepcopy(molecule.acids)
    while i < x:
        print(i)
        backupseqence = copy.deepcopy(molecule.acids)

        #make a random turn
        randomnode = random.randint(0, len(molecule.acids) - 1)
        randomdirection = random.randint(0, 1)
        if randomdirection == 0:
            randomdirection = 'Right'
        else:
            randomdirection = 'Left'
        molecule.turn(randomnode, randomdirection)

        #check if the resulting turn is valid
        if not molecule.check_vadility():
            print("notvalid")
            molecule.acids = backupseqence
        elif lowest > molecule.stability():
            print("replacing")
            lowest = molecule.stability()
            lowestsequence = copy.deepcopy(molecule.acids)
        i = i + 1

    molecule.acids = lowestsequence
