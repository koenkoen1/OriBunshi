import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "objects"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "results"))

from depth import depth
from greedyadd import greedyadd
from greedyfold import spiralfold
from molecule import Molecule
from randomturns import randomturns
from annealing import anneal
from randomsample import randomsample

directions = ["Left", "Right"]


def load_sequence():
    """
    Asks user for a sequence, which can be custom or one of the standard
    sequences. Returns the sequence obtained.
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


def load_molecuel(sequence):
    """
    Prompts user to choose a method to loads molecule with chosen sequence, and
    loads molecule via that method.
    """

    # prompt user for molecule loading method and validate input
    method = input("Molecule loading method" \
                   "(direct, acids, greedyadd, depth, random): ")
    molecule = 0
    if method == 'direct' or method == 'acids':
        molecule = Molecule(sequence, method)
    elif method == 'greedyadd':
        molecule = Molecule([], "direct")
        greedyadd(molecule, sequence)
        print(f"stability: {molecule.stability()}")
    elif method == "depth":
        molecule = depth(sequence)
    elif method == "random":
        molecule = Molecule(sequence, method)
    else:
        print('No valid loading method.')
        return load_molecuel(sequence)
    return molecule


def main():
    """
    Gets sequence from load_sequence function, loads sequence into datastructure.
    Then waits for command from user. Executes specified command if valid.
    """
    sequence = load_sequence()
    molecule = load_molecuel(sequence)

    while True:
        # prompt user for command
        command = input("command: ").split()

        if command[0] == "quit":
            break

        elif command[0] == "spiral":
            spiralfold(molecule, len(sequence))
            print(f"stability: {molecule.stability()}")

        elif command[0] == "anneal":
            save_data = False

            # check if the save command was given, if so let anneal save data
            try:
                if command[1] == "save":
                    save_data = True
                else:
                    print(f"Error: {command[1]} is not accepted."
                          "Usage: anneal (save)")
            except IndexError:
                pass

            molecule = anneal(molecule, save_data)
            molecule.draw()

        elif command[0] == "sample":
            iterations = ''
            save_data = False

            # check for errors and convert to convert variables to proper format
            try:
                iterations = int(command[1])
            except ValueError:
                print(f"Error: {command[1]} is not a number")
                continue
            except IndexError:
                print("use: random iterations (save)")
                continue

            # check if save command was given, if so let randomsaple save data
            try:
                if command[2] == "save":
                    save_data = True
                else:
                    print(f"Error: {command[2]} is not accepted."
                          "Usage: random iterations (save)")
            except IndexError:
                pass

            randomsample(molecule.sequence, iterations, save_data)

        elif command[0] == "random":
            iterations = ''

            # check for errors and convert to convert variables to proper format
            try:
                iterations = int(command[1])
            except ValueError:
                print(f"Error: {command[1]} is not a number")
                continue
            except IndexError:
                print("use: random iterations")
                continue

            randomturns(molecule, iterations)
            print(f"stability: {molecule.stability()}")

        # plot a graph to visualize protein
        elif command[0] == "draw":
            molecule.draw()

        elif command[0] == "turn":
            # check for errors and convert to convert variables to proper format
            try:
                position = int(command[2]) - 1
            except ValueError:
                print(f"Error: {command[2]} is not a number")
                continue
            except IndexError:
                print("use: turn direction number")
                continue
            direction = command[1].lower().capitalize()

            # turn molecule at given position towards direction 'direction'
            if direction in directions:
                if position < len(sequence) and position > -1:
                    molecule.turn(position, direction)
                    print(f"stability: {molecule.stability()}")
                    print(f"valid?: {molecule.check_vadility()}")
                else:
                    print("invalid number")
            else:
                print("direction can only be left or right")

        elif command[0] == "force_vadil":
            molecule.force_vadil()
            molecule.draw()

        elif command[0] == 'help':
            print("turn: turns the molecule (ie: turn 2 Left)")
            print("random: turns the molecule randomly (usage: random 10)")
            print("draw: draws the molecule (usage: draw)")
            print("spiral: turns the molecule into a spiral (usage: spiral)")
            print("anneal: performs the 'simulated annealing' algorithm on the"\
                  " molecule (usage: anneal (save))")
            print("sample: get best out of given number of samples")
            print("quit: quits the application")
        else:
            print("invalid command")


if __name__ == "__main__":
    main()
