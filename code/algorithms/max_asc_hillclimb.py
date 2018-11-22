import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

from molecule import Molecule

def climb(molecule):
    # TODO
    pass

if __name__ == '__main__':
    molecule = Molecule('HPHPPPHPHPHP', 'direct')
    climb(molecule)
    molecule.draw()
