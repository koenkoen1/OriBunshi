import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "helpers"))
sys.path.append(os.path.join(directory, "code", "objects"))
sys.path.append(os.path.join(directory, "results"))


from depth import depth
from greedyfold import spiralfold
from molecule import Molecule
from annealing import anneal
from hillclimb import hillclimb
from randomsample import randomsample
from populationbased import populationbased

def load_sequence():
    """
    Asks user for a sequence, which can be custom or one of the standard
    sequences. Returns the sequence obtained.
    """
    method = input("type of amino acid sequence(standard, custom): ")

    if method == 'custom':
        sequence = "O"
        # ask for sequence, reject letters other than H and P
        while any(c not in 'HPC' for c in sequence):
            sequence = input("sequence(consisting of H's, C's, and P's): ")
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
        # ask again if method is invalid
        return load_sequence()


def load_molecuel(sequence):
    """
    Prompts user to choose a method to loads molecule with chosen sequence, and
    loads molecule via that method.
    """

    # prompt user for molecule loading method and validate input
    method = input("Molecule loading method (direct, acids, depth, random): ")
    molecule = 0
    if method == 'direct' or method == 'acids':
        molecule = Molecule(sequence, method)
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
    Gets sequence and molecule object from load functions.
    Then waits for command from user. Executes specified command if valid.
    """
    sequence = load_sequence()
    molecule = load_molecuel(sequence)
    directions = ["Left", "Right"]

    while True:
        # prompt user for command
        command = input("command: ").split()

        if not command:
            continue

        elif command[0] == "quit":
            break

        elif command[0] == "spiral":
            spiralfold(molecule)
            print(f"stability: {molecule.stability()}")

        elif command[0] == "stoch_climb":
            iterations = ''
            save_data = False

            # check for errors and convert to convert variables to proper format
            try:
                iterations = int(command[1])
            except ValueError:
                print(f"Error: {command[1]} is not a number")
                continue
            except IndexError:
                print("Usage: stoch_climb iterations (save)")
                continue

            # check if the save command was given, if so save data
            try:
                if command[2] == "save":
                    save_data = True
                else:
                    print(f"Error: {command[1]} is not accepted." \
                          "\nUsage: stoch_climb iterations (save)")
            except IndexError:
                pass

            hillclimb(molecule, iterations, save_data)
            molecule.draw()

        elif command[0] == "anneal":
            reheat_times = ''
            reheat_temp = ''
            save_data = False

            # check for errors and convert to convert variables to proper format
            try:
                reheat_times = int(command[1])
            except ValueError:
                print(f"Error: {command[1]} is not a number")
                continue
            except IndexError:
                print("Usage: anneal reheat_times reheat_temp (save)")
                continue

            try:
                reheat_temp = int(command[2])
            except ValueError:
                print(f"Error: {command[2]} is not a number")
                continue
            except IndexError:
                print("Usage: anneal reheat_times reheat_temp (save)")
                continue

            # check if the save command was given, if so let anneal save data
            try:
                if command[3] == "save":
                    save_data = True
                else:
                    print(f"Error: {command[1]} is not accepted." \
                          "\nUsage: anneal reheat_times reheat_temp (save)")
            except IndexError:
                pass

            molecule = anneal(molecule, reheat_times, reheat_temp, save_data)
            molecule.draw()

        elif command[0] == "population":
            popsize = ''
            gens = ''
            save_data = False

            # check for errors and convert to convert variables to proper format
            try:
                popsize = int(command[1])
            except ValueError:
                print(f"Error: {command[1]} is not a number")
                continue
            except IndexError:
                print("Usage: population popsize generations (save)")
                continue

            try:
                gens = int(command[2])
            except ValueError:
                print(f"Error: {command[2]} is not a number")
                continue
            except IndexError:
                print("Usage: population popsize generations (save)")
                continue

            # check if the save command was given, if so let pop save data
            try:
                if command[3] == "save":
                    save_data = True
                else:
                    print(f"Error: {command[3]} is not accepted."
                          "Usage: population popsize generations (save)")
            except IndexError:
                pass

            molecule = populationbased(sequence, popsize, gens, save_data)
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

            molecule = randomsample(molecule, iterations, save_data)
            molecule.draw()

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
            print("turn: turns the molecule (usage: turn Left 2)" \
                  "\nrandom: turns the molecule randomly (usage: random 10)" \
                  "\ndraw: draws the molecule (usage: draw)" \
                  "\nspiral: turns the molecule into a spiral (usage: spiral)" \
                  "\nstoch_climb: performs a 'stochastic hill climber " \
                  "algorithm' on the molecule (usage: stoch_climb iterations "\
                  "(save))"
                  "\nanneal: performs the 'simulated annealing' algorithm on " \
                  "the molecule (usage: anneal (save))" \
                  "\nsample: get best out of given number of samples" \
                  "\npopulation: run a population based algorithm on the " \
                  "molecule (usage: population popsize generations (save))" \
                  "\nquit: quits the application")
        else:
            print("invalid command")


if __name__ == "__main__":
    main()
