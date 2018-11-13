from amino_acid import Amino_Acid
import matplotlib.pyplot as plt

class Molecule(object):

    # init function saves sequence and produces coordinates
    def __init__(self, sequence):
        self.sequence = []
        coordinates = x, y = (0, 0)

        # produces a list of amino acids with coordinates (0, 0), (0, 1) etc
        for letter in sequence:
            self.sequence.append(Amino_Acid(letter, coordinates))
            x = x + 1
            coordinates = (x, y)

    # produces a printable representation of a molecule
    def __str__(self):
        string = ''
        for amino_acid in self.sequence:
            string = string + str(amino_acid)
        return string

    # returns the stability of the molecule
    def stability(self):
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

    # Checks for nodes with the same coordinates
    def check_vadility(self):
        #for every amino acid look at every amino acid
        for amino_acid in self.sequence:
            for amino_acid2 in self.sequence:

                # if they are not the same
                if amino_acid != amino_acid2:

                    # check if the coordinates are the same
                    if amino_acid.coordinates == amino_acid2.coordinates:
                        return False
        return True

    # Draws an image of the molecule on screen
    def draw(self):
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

            plt.plot(amino_acid.coordinates[0], amino_acid.coordinates[1], '-o', c=color, markersize=10)
        plt.xticks(range( -len(self.sequence), len(self.sequence) ))
        plt.yticks(range( -len(self.sequence), len(self.sequence) ))
        # shows the plot
        plt.show()
        return True
