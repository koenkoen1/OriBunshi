import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))


from molecule import Molecule

molecule = Molecule("AAAAAAAAAAAAAAAAAAAAAAAAAa")


print(molecule)
