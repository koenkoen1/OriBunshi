import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "objects"))

from molecule import Molecule

def main():
    # gib fir lin
    with open('data/input.txt', 'r') as input:
        line = input.readline()
        mol = Molecule(line)
        print(mol)

if __name__ == "__main__":
    main()
