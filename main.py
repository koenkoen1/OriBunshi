import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "objects"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from depth import depth
from greedyadd import greedyadd
from greedyfold import spiralfold
from molecule import Molecule
from randomturns import randomturns
from depth import depth

directions = ["Left", "Right"]


def load_sequence():
    """
    Asks user for a sequence, which can be custom or one of the standard
    sequences. Returns the sequence obtained
    """
    method = input("type of amino acid sequence(standard, custom): ")

    if method == 'custom':
        sequence = "O"
        # ask for sequence, reject letters other than H and P
        while any(c not in 'HP' for c in sequence):
            sequence = input("sequence(consisting of H's and P's): ")
        print(f"\ncurrent sequence is {sequence}")
        return sequence

    elif method == 'standard':
        with open('data/input.txt', 'r') as f:
            # parse possible sequences
            options = {}
            lines = f.readlines()
            print("options:")
            for i in range(len(lines)):
                options[i] = lines[i].rstrip('\n')
                print(f"{i}: {lines[i]}", end='')

            # ask for key of sequence, only accept integers
            key = -1
            while key > len(lines) - 1 or key < 0:
                try:
                    key = int(input("select sequence: "))
                except:
                    print("Invalid number")
                    pass
            print(f"\ncurrent sequence is {options[key]}")
            return options[key]

    else:
        return load_sequence()

def main():
    sequence = load_sequence()

    # prompt user for molecule loading method and validate input
    method = input("Molecule loading method (direct, acids, greedyadd, depth): ")
    if method == 'direct' or method == 'acids':
        molecule = Molecule(sequence, method)
    elif method == 'greedyadd':
        molecule = Molecule([], "direct")
        greedyadd(molecule, sequence)
        print(f"stability: {molecule.stability()}")
    elif method == "depth":
        molecule = depth(sequence)
    else:
        print('No valid loading method.')
        return 1

    while True:

        # prompt user for command
        command = input("command: ").split()

        if command[0] == "quit":
            break

        elif command[0] == "spiral":
            spiralfold(molecule, len(sequence))
            print(f"stability: {molecule.stability()}")

        elif len(command) == 2 and command[0] == "random":
            randomturns(molecule, int(command[1]))
            print(f"stability: {molecule.stability()}")

        elif command[0] == "draw":
            molecule.draw()

        elif (len(command) == 3):
            try:
                # check whether id is a number and convert to int
                id = int(command[1]) - 1
            except ValueError:
                print("id was not a number")

            # convert direction to required format
            direction = command[2].lower().capitalize()

            # turn molecule at position 'id' towards direction 'direction'
            if command[0] == "turn" and direction in directions:
                if id < len(sequence) and id > -1:
                    molecule.turn(id, direction)
                    print(f"stability: {molecule.stability()}")
                    print(f"valid?: {molecule.check_vadility()}")
                else:
                    print("invalid id")
            else:
                print("use: turn id direction")
        elif command[0] == 'Help':
            print("turn turns the molecule (ie: turn 2 Left)")
            print("random: turns the molecule randomly (usage: random 10)")
            print("draw: draws the molecule (usage: draw)")
            print("spiral: turns the molecule into a spiral (usage: spiral)")
        else:
            print("invalid command")


if __name__ == "__main__":
    main()
