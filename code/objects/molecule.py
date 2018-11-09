from amino_acid import Amino_Acid
import matplotlib.pyplot as plt

class Molecule(object):

    def __init__(self, sequence, method):
    """
    Itializes a molecule. Saves sequence and calls a loading methodself.
    """
        self.sequence = []

        if method == 'direct':
            load_direct()
        elif method == 'acids':
            load_acids()
        else:
            print('No valid loading method.')


    def __str__(self):
    """
    Produces a printable representation of a molecule.
    """
        string = ''
        for amino_acid in self.sequence:
            string = string + str(amino_acid)
        return string


    def load_direct(self):
    """
    Loads molecule as a whole, in a straight configuration.
    """

        # initialize coordinates for first amino acid
        coordinates = x, y = (0, 0)

        # adds amino acids with coordinates (0, 0), (0, 1), etc. to sequence
        for letter in sequence:
            self.sequence.append(Amino_Acid(letter, coordinates))
            x += 1
            coordinates = (x, y)


    def load_acids(self):
    """
    Loads molecule, by adding one amino acid at a time at given coordinates.
    """

        for letter in sequence:

            valid_xy = False

            # promt for coordinates until they're valid
            while not valid_xy:

                # promt user for coordinates
                x = int(input("x coordinate: "))
                y = int(input("y coordinate: "))

                # check validity of coordinates
                if x and y not integers (or digits):
                    print("Please enter integers.")
                elif not ((acid.coordinates[0] - x == 0 and
                           abs(acid.coordinates[1] - y == 1)) or
                          (abs(acid.coordinates[0] - x == 1) and
                           acid.coordinates[1] - y == 0)):
                    print("Amino acid must border previous one.")
                else:
                    valid_xy = True

            coordinates = (x, y)

            acid = Amino_Acid(letter, coordinates)
            self.sequence.append(acid)
            print("Amino acid added.")


        # TODO
        # kan wellicht in zelfde method als direct, waarbij je of algoritme moet
        # laten werken tijdens opbouw, of rechte lijn opbouwen (en dan algoritme)


    def stability(self):
    """
    Calculates and returns the stability of a molecule.
    """

        stability = 0

        #For every amino acid check every amino acid
        for amino_acid in self.sequence:
            for amino_acid2 in self.sequence:

                # check if they are both 'H' (they only produce stability)
                if amino_acid.kind == 'H' and amino_acid2.kind == 'H':

                        # if the amino acids are not the same and next to eachother in the list
                        if (amino_acid != amino_acid2) and abs(self.sequence.index(amino_acid2) - self.sequence.index(amino_acid)) != 1:
                            rest = (amino_acid.coordinates[0] -
                                    amino_acid2.coordinates[0],
                                    amino_acid.coordinates[1] -
                                    amino_acid2.coordinates[1])

                            # if they are next to eachother increase stability
                            if (abs(rest[0]) == 1 and rest[1] == 0) or (abs(rest[1]) == 1 and rest[0] == 0):
                                stability = stability - 1
        return stability / 2


    def turn(self, nodelocation, direction):
    """
    Turns the molecule from given node in given direction.
    """

        # save the relative locatin of the turn
        relativelocation = self.sequence[nodelocation].coordinates

        # while there are still nodes after the nodelocation
        while nodelocation < len(self.sequence) - 1:
            nodelocation = nodelocation + 1

            # save the relative locations and a temp value
            location = self.sequence[nodelocation].coordinates
            relativex = location[0] - relativelocation[0]
            relativey = location[1] - relativelocation[1]
            temp = relativex

            # if the direction equals left x = -y and y = x (relative)
            if direction == 'Left':
                relativex = -relativey + relativelocation[0]
                relativey = temp  + relativelocation[1]

            # if the direction equals Right x = y and y = -x (relative)
            elif direction == 'Right':
                relativex = relativey + relativelocation[0]
                relativey = -temp + relativelocation[1]
            else:
                return False
            # save the new location
            self.sequence[nodelocation].coordinates = (relativex, relativey)
        return True


    def check_vadility(self):
    """
    Checks if molecule configuration is valid, by checking for nodes with the
    same coordinates. Returns a boolean.
    """

        #for every amino acid look at every amino acid
        for amino_acid in self.sequence:
            for amino_acid2 in self.sequence:

                # if they are not the same
                if amino_acid != amino_acid2:

                    # check if the coordinates are the same
                    if amino_acid.coordinates == amino_acid2.coordinates:
                        return False
        return True


    def draw(self):
    """
    Makes a visual representation of the molecule, using matplotlib.
    """

        oldx = 100
        oldy = 100
        xcoordinates = []
        ycoordinates = []

        # draws the lines between the amino acid sequence
        for amino_acid in self.sequence:
            xcoordinates.append(amino_acid.coordinates[0])
            ycoordinates.append(amino_acid.coordinates[1])
        plt.plot(xcoordinates, ycoordinates, c='black')

        # draws the dots in the amino acid sequence
        for amino_acid in self.sequence:
            if amino_acid.kind == 'H':
                color = 'r'
            else:
                color = 'b'

            plt.plot(amino_acid.coordinates[0], amino_acid.coordinates[1], '-o', c=color)

        # shows the plot
        plt.show()
        return True
