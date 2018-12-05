from amino_acid import Amino_Acid
import matplotlib.pyplot as plt
import random


class Molecule(object):

    def __init__(self, sequence, method):
        """
        Initializes a molecule. Saves sequence and calls a loading method.
        """
        self.sequence = sequence
        self.acids = []

        if method == 'direct':
            self.load_direct()
        elif method == 'acids':
            self.load_acids()
        elif method == 'random':
            self.load_random(self.sequence)
        else:
            print('No valid loading method.')


    def add_acids(self, acids, update_seq = True):
        """
        Adds given amino acids to molecule. Returns True if it was a valid
        placement, else False.
        """

        for amino_acid in acids:
            self.acids.append(amino_acid)

            if not self.check_vadility():
                self.acids.pop()
                return False
            if update_seq:
                self.sequence += amino_acid.kind

        return True


    def check_vadility(self, return_conflicts = False):
        """
        Checks if molecule configuration is valid, by checking for nodes with
        the same coordinates. Returns a boolean.
        """

        # for every amino acid look at every other amino acid
        for index1, amino_acid in enumerate(self.acids):
            for index2, amino_acid2 in enumerate(self.acids):
                if amino_acid != amino_acid2:

                    # check if the coordinates are the same
                    if amino_acid.coordinates == amino_acid2.coordinates:
                        if return_conflicts:
                            return [index1, index2]
                        return False

        if return_conflicts:
            return None
        return True


    def draw(self):
        """
        Makes a visual representation of the molecule, using matplotlib.
        """
        previous  = x, y = 100, 100
        xcoordinates = []
        ycoordinates = []
        Hxcoordinates = []
        Hycoordinates = []
        Cxcoordinates = []
        Cycoordinates = []

        # draws the lines between the amino acid sequence
        for amino_acid in self.acids:
            if amino_acid.kind == 'H':
                Hxcoordinates.append(amino_acid.coordinates[0])
                Hycoordinates.append(amino_acid.coordinates[1])
            elif amino_acid.kind == 'C':
                Cxcoordinates.append(amino_acid.coordinates[0])
                Cycoordinates.append(amino_acid.coordinates[1])
            else:
                xcoordinates.append(amino_acid.coordinates[0])
                ycoordinates.append(amino_acid.coordinates[1])
            if previous[0] != 100:
                plt.plot([amino_acid.coordinates[0], previous[0]],
                         [amino_acid.coordinates[1], previous[1]],
                         color='black')
            previous = amino_acid.coordinates[0], amino_acid.coordinates[1]

        # for every amino acid check every amino acid
        for amino_acid in self.acids:
            for amino_acid2 in self.acids:

                # check if they are both 'H' (they only produce stability)
                if amino_acid.kind == 'H' and amino_acid2.kind == 'H':

                    # check if amino acids are not the same nor sequent
                    if ((amino_acid != amino_acid2)
                        and abs(self.acids.index(amino_acid2)
                            - self.acids.index(amino_acid)) != 1):
                        rest = (amino_acid.coordinates[0] -
                                amino_acid2.coordinates[0],
                                amino_acid.coordinates[1] -
                                amino_acid2.coordinates[1])

                        # draw line marking connections between amino acids
                        if ((abs(rest[0]) == 1 and rest[1] == 0)
                            or (abs(rest[1]) == 1 and rest[0] == 0)):
                            plt.plot([amino_acid.coordinates[0],
                                      amino_acid2.coordinates[0]],
                                     [amino_acid.coordinates[1],
                                      amino_acid2.coordinates[1]],
                                     color="r", linestyle=':')

        plt.plot(Hxcoordinates, Hycoordinates, 'o', label='H', color='r',
                 markersize=10)
        plt.plot(Cxcoordinates, Cycoordinates, 'o', label='C', color='g',
                 markersize=10)
        plt.plot(xcoordinates, ycoordinates, 'o', label='P', color='b',
                 markersize=10)
        plt.legend()
        plt.suptitle(f"Stability = {self.stability()}", fontweight='bold')
        plt.title(f"sequence = {self.sequence}", fontsize=10)

        # shows the plot
        plt.show()


    def force_vadil(self):
        """
        Forces molecule in valid configuration after invalid turn. Returns True
        if successful, else False.
        """

        # find indexes of first collision
        indexes = self.check_vadility(True);

        # continue until there are no collisions
        while indexes:

            # get random turning direction
            dir = ["Left", "Right"]
            random.shuffle(dir)

            compare = indexes[1]

            self.turn(indexes[1] - 1, dir[0])
            indexes = self.check_vadility(True)

            # prevent direct movement back to previous configuration
            if indexes and indexes[1] == compare:
                self.turn(indexes[1] - 1, dir[1])
                indexes = self.check_vadility(True)

                # if turning index[1] + 1 proves unsuccessful, try index[0] + 1
                if indexes and indexes[1] == compare:
                    compare = indexes[0]
                    self.turn(indexes[0] + 1, dir[0])
                    indexes = self.check_vadility(True)

                    # prevent direct movement back to previous configuration
                    if indexes and indexes[0] == compare:
                        self.turn(indexes[0] + 1, dir[1])
                        indexes = self.check_vadility(True)

                        # if index[0] + 1 also unsuccessful, turn random index
                        if indexes and indexes[0] == compare:
                            self.turn(random.randint(indexes[0] + 1, indexes[1]),
                                      dir[0])
                            indexes = self.check_vadility(True)
        return True


    def load_acids(self):
        """
        Initializes acid list attribute, asks for user input for x- and
        y-positions of every amino_acid object being created. Creates amino_acid
        objects based on the sequence attribute and their coordinates. They are
        then appended to the acids list.
        """

        # initialize "phantom" amino acid, to check if acid is first in sequence
        acid = Amino_Acid('first', (0, 0))

        # let user add every amino acid in sequence at desired coordinates
        for letter in self.sequence:

            valid_xy = False

            # promt user for coordinates until they're valid
            while not valid_xy:

                # promt user for coordinates
                x = input("x coordinate: ")
                y = input("y coordinate: ")

                # proceed if user entered integers
                try:
                    x = int(x)
                    y = int(y)

                    # check if amino acid neighbors previous amino acid
                    if ((acid.coordinates[0] - x == 0
                         and abs(acid.coordinates[1] - y) == 1)
                        or (abs(acid.coordinates[0] - x) == 1
                            and acid.coordinates[1] - y == 0)
                        or acid.kind == "first"):

                        coordinates = (x, y)

                        temp_acid = Amino_Acid(letter, coordinates)
                        self.acids.append(temp_acid)

                        # check if coordinates are free, if so add amino acid
                        if self.check_vadility():
                            valid_xy = True
                            acid = temp_acid
                            print("Amino acid added.")
                        else:
                            self.acids.remove(temp_acid)
                            print("Place already contains amino acid.")

                    else:
                        print("Amino acid must neighbor previous one.")

                except ValueError:
                    print("Please enter integers.")

        # possibility: enter list of coordinates and read it oid
        # (then also load_direct and load_acids can be merged)


    def load_direct(self):
        """
        Initializes acid list attribute: Creates amino_acid objects based on
        sequence attribute and with arbitrary coordinates. Adds created
        amino_acid objects to acid list.
        """

        # initialize coordinates for first amino acid
        coordinates = x, y = (0, 0)

        # adds amino acids with coordinates (0, 0), (0, 1), etc. to sequence
        for letter in self.sequence:
            self.acids.append(Amino_Acid(letter, coordinates))
            x += 1
            coordinates = (x, y)

        # print(self)


    def load_random(self, sequence):
        """
        Loads a random configuration of molecule's sequence.
        """
        self.sequence = ""
        # load first two acids at (0, 0) and (1, 0)
        self.add_acids([Amino_Acid(sequence[0], (0, 0)),
                        Amino_Acid(sequence[1], (1, 0))], True)

        copy_seq = sequence[2:]

        # load rest of acids at random neighbouring place to previous acid
        for letter in copy_seq:

            # print(letter)

            # get random direction to place next acid into
            dir = [0, 1, 2, 3]
            random.shuffle(dir)

            # iterate until successful add of new acid
            for i in range(4):
                x, y  = self.acids[len(self.acids) - 1].coordinates
                # print(x, y)

                # translate direction into coordinate change
                if dir[i] == 0:
                    x += 1
                elif dir[i] == 1:
                    y += 1
                elif dir[i] == 2:
                    x -= 1
                else:
                    y -= 1

                # if successful add: stop inner for loop
                if self.add_acids([Amino_Acid(letter, (x, y))], False):
                    self.sequence += letter
                    break

                # if at end inner forloop no add: accept invalid, force to valid
                elif i == 3:
                    self.acids.append(Amino_Acid(letter, (x, y)))
                    self.sequence += letter
                    self.force_vadil()

        return True


    def stability(self):
        """
        Calculates and returns the stability of a molecule.
        """

        stability = 0

        # for every amino acid check every amino acid
        for amino_acid in self.acids:
            for amino_acid2 in self.acids:

                # check if they are both 'H' (they only produce stability)
                if amino_acid.kind == 'H' and amino_acid2.kind == 'H':

                    # check if amino acids are not the same nor sequent
                    if ((amino_acid != amino_acid2)
                        and abs(self.acids.index(amino_acid2)
                            - self.acids.index(amino_acid)) != 1):
                        rest = (amino_acid.coordinates[0] -
                                amino_acid2.coordinates[0],
                                amino_acid.coordinates[1] -
                                amino_acid2.coordinates[1])

                        # if they are next to eachother increase stability
                        if ((abs(rest[0]) == 1 and rest[1] == 0)
                            or (abs(rest[1]) == 1 and rest[0] == 0)):
                            stability = stability - 1

        return int(stability / 2)


    def remove_acids(self, acids):
        """
        Removes given amino acids from molecule.
        """

        for amino_acid in acids:
            self.acids.remove(amino_acid)
            self.sequence = self.sequence[:-1]


    def turn(self, nodelocation, direction):
        """
        Changes the coordinates of every amino_acid past the given
        nodelocation to turn the molecule from that point to the given
        direction. Returns False if the direction is not valid, else returns
        True once the amino_acids have been moved.
        """

        # save the relative locatin of the turn
        relativelocation = self.acids[nodelocation].coordinates

        # while there are still nodes after the nodelocation
        while nodelocation < len(self.acids) - 1:
            nodelocation = nodelocation + 1

            # save the relative locations and a temp value
            location = self.acids[nodelocation].coordinates
            relativex = location[0] - relativelocation[0]
            relativey = location[1] - relativelocation[1]
            temp = relativex

            # if the direction equals left x = -y and y = x (relative)
            if direction == 'Left':
                relativex = -relativey + relativelocation[0]
                relativey = temp + relativelocation[1]

            # if the direction equals Right x = y and y = -x (relative)
            elif direction == 'Right':
                relativex = relativey + relativelocation[0]
                relativey = -temp + relativelocation[1]
            else:
                return False

            # save the new location
            self.acids[nodelocation].coordinates = (relativex, relativey)

        return True


    def __str__(self):
        """
        Defines how to print an Molecule object. Returns a string.
        """

        amino_acids = []
        for amino_acid in self.acids:
            amino_acids.append(str(amino_acid))
        string = "\n".join(amino_acids)

        return string


    def force_valid(self):
        """
        Forces molecule in valid configuration after invalid turn. Returns True
        if successful, else False.
        """

        # find indexes of first collision
        indexes = self.check_vadility(True);

        i = 1
        # continue until there are no collisions
        while indexes:
            dir = ['Left', 'Right']
            random.shuffle(dir)
            self.turn(indexes[0] + i, dir[0])
            indexes = self.check_vadility(True);
            if not indexes:
                break
            self.turn(indexes[1] - i, dir[0])
            indexes = self.check_vadility(True);
            if not indexes:
                break
            i += 1
            if indexes[1] - i <= indexes[0]:
                i = 1
        return True
