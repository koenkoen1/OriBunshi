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
from greedyclimb import climb
from annealing import copylocations 

sequence = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
#  rip dit
# properties [[[movement, velocity],..], personalbest, personalbestmovement]
def particleswarm(sequence):
    pop = []
    properties = []
    stagbest = 1
    gbest = 0
    w = 0.5
    for i in range(100):
        molecule = Molecule(sequence, "random")
        pop.append(molecule)
        properties.append([notate(molecule), 1, 1])
    x = 0
    while x < 500:
        for index, molecule in enumerate(pop):

            # pbest
            if properties[index][1] > molecule.stability():
                properties[index][1] = molecule.stability()
                properties[index][2] = properties[index][0]

            # gbest
            if stagbest > molecule.stability():
                stagbest = molecule.stability()
                gbest = properties[index][0]
            for indexx, location in enumerate(properties[index][0]):
                r1 = random.uniform(0,1)
                r2 = random.uniform(0,1)
                location[1] = location[1] * w + r1 * 1.3 * (gbest[indexx][0] - location[0]) + r2 * 1.3 * (properties[index][2][indexx][0] - location[0])
                location[0] = int(location[0]  + location[1])
                print(location[1])
            molecule, properties[index][0]  = transform(properties[index][0])
        x += 1
    transform(gbest)[0].draw()

def notate(molecule):
    movement = []
    for index, acid in enumerate(molecule.acids):
        if index != 0:
            nextcoordinates = acid.coordinates
            previouscoordinates = molecule.acids[index - 1].coordinates
            differencex = nextcoordinates[0] - previouscoordinates[0]
            differencey = nextcoordinates[1] - previouscoordinates[1]
            if differencex == 1:
                movement.append([1, 1])
            elif differencey == 1:
                movement.append([2, 1])
            elif differencex == -1:
                movement.append([3, 1])
            else:
                movement.append([4, 1])
    return movement

def transform(locations):
    x = 0
    y = 0
    molecule = Molecule(sequence[0], "direct")
    for index, location in enumerate(locations):
        if location[0] == 1:
            x += 1
        elif location[0] == 2:
            y += 1
        elif location[0] == 3:
            x -= 1
        elif location[0] == 4:
            y -= 1
        else:
            print(location[0])
        molecule.acids.append(Amino_Acid(sequence[index + 1], (x, y)))
        molecule.sequence += sequence[index + 1]
    if not  molecule.check_vadility():
        molecule.force_vadil()
        locations = notate(molecule)
        print("lol")
    return (molecule, locations)

def getbest(properties):
    lowest = 0
    for property in properties:
        if property[2] < lowest:
            lowest = property[2]
    return lowest
if __name__ == '__main__':
    particleswarm("PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP")
