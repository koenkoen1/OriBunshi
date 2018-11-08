import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "objects"))

from molecule import Molecule

directions = ["Left", "Right"]

def load_sequence():
    """
    gives first line of input.txt
    """
    with open('data/input.txt', 'r') as f:
        line = f.readline()
        print(f"current sequence is {line}")
<<<<<<< HEAD
        molecule = Molecule(line)
        molecule.draw()
        command = input("command: ")
=======
        return line

def main():
    sequence = load_sequence()
    molecule = Molecule(sequence)

    while True:
        # ask for user input
        command = input("command: ").split()
>>>>>>> 950c2644df55b566f29084958f4afebb268516b0

        if command[0] == "quit":
            break

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
                else:
                    print("id too high for sequence")
            else:
                print("use: turn id direction")
        else:
            print("invalid command")


if __name__ == "__main__":
    main()
