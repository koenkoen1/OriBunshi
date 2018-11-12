from amino_acid import Amino_Acid
import matplotlib.pyplot as plt


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
        else:
            print('No valid loading method.')

    def add_acids(self, specifications):
        """
        Adds amino acids with given specifiactions to molecule. Takes a
        dictionary of format {letter: coordinates} as argument.
        Returns a boolean.
        """

        for letter in specifications:
            amino_acid = Amino_Acid(letter, specifications[letter])
            self.acids.append(amino_acid)

            if not self.check_vadility:
                self.acids.remove(amino_acid)
                return False

        return True

    def check_vadility(self):
        """
        Checks if molecule configuration is valid, by checking for nodes with
        the same coordinates. Returns a boolean.
        """

        # for every amino acid look at every other amino acid
        for amino_acid in self.acids:
            for amino_acid2 in self.acids:
                if amino_acid != amino_acid2:

                    # check if the coordinates are the same
                    if amino_acid.coordinates == amino_acid2.coordinates:
                        return False

        return True

    def draw(self):
        """
        Makes a visual representation of the molecule, using matplotlib.
        (Why does it return a boolean?)
        """

        oldx = 100
        oldy = 100
        xcoordinates = []
        ycoordinates = []

        # draws the lines between the amino acid sequence
        for amino_acid in self.acids:
            xcoordinates.append(amino_acid.coordinates[0])
            ycoordinates.append(amino_acid.coordinates[1])
        plt.plot(xcoordinates, ycoordinates, c='black')

        # draws the dots in the amino acid sequence
        for amino_acid in self.acids:
            if amino_acid.kind == 'H':
                color = 'r'
            else:
                color = 'b'

            plt.plot(amino_acid.coordinates[0], amino_acid.coordinates[1],
                     '-o', c=color)

        # shows the plot
        plt.show()
        return True

    def load_acids(self):
        """
        Loads molecule, by adding one amino acid at a time at given coordinates.
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
        Loads molecule as a whole, in a straight configuration.
        """

        # initialize coordinates for first amino acid
        coordinates = x, y = (0, 0)

        # adds amino acids with coordinates (0, 0), (0, 1), etc. to sequence
        for letter in self.sequence:
            self.acids.append(Amino_Acid(letter, coordinates))
            x += 1
            coordinates = (x, y)

        print(self)

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

        return stability / 2

    def remove_acids(self, specifications):
        """
        Removes amino acids with given specifiactions from molecule. Takes a
        dictionary of format {letter: coordinates} as argument.
        """

        for letter in specifications:
            amino_acid = Amino_Acid(letter, specifications[letter])
            self.acids.remove(amino_acid)

    def turn(self, nodelocation, direction):
        """
        Turns the molecule from given node in given direction.
        (Why does this return a boolean?)
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
        Produces a printable representation of a molecule.
        """

        string = ''

        for amino_acid in self.acids:
            string = string + str(amino_acid)

        return string
