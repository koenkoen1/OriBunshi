import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "objects"))

from molecule import Molecule

directions = ["left", "right"]

def main():
    # gib fir lin
    with open('data/input.txt', 'r') as f:
        line = f.readline()
        print(f"current sequence is {line}")
        molecule = Molecule(line)
        command = input("command: ")

        try:
            command = command.split()
        except:
            print("use: turn id direction")

        if (command[0] == "turn" and len(command) == 3 and
            command[2] in directions):
            try:
                id = int(command[1])
                molecule.turn(id, command[2])
                print(molecule.stability())
            except ValueError:
                print("id was not a number")
        else:
            print("use: turn id direction")


if __name__ == "__main__":
    main()
