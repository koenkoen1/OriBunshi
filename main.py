import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "objects"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from molecule import Molecule
from randomturns import randomturns

directions = ["Left", "Right"]

def load_sequence():
    """
    gives first line of input.txt
    """
    with open('data/input.txt', 'r') as f:
        line = f.readline()
        print(f"current sequence is {line}")
        return line

def main():
    sequence = load_sequence()
    molecule = Molecule(sequence)

    while True:
        # ask for user input
        command = input("command: ").split()

        if command[0] == "quit":
            break

        if len(command) == 2 and command[0] == "random":
            try:
                randomturns(molecule, int(command[1]))
            except:
                print("one does not simply")

        elif command[0] == "draw":
            molecule.draw()

        elif (len(command) == 3):
            # check whether id is a number and convert to int
            try:
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
                    print("id too high for sequence")
            else:
                print("use: turn id direction")
        else:
            print("invalid command")


if __name__ == "__main__":
    main()
