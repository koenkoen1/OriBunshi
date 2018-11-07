from amino_acid import Amino_Acid

class Molecule(object):

    # init function
    def __init__(self, sequence):
        self.sequence = []
        coordinates = x, y = (0, 0)

        # produces a list of amino acids with coordinates (0, 0), (0, 1) etc
        for letter in sequence:
            self.sequence.append(Amino_Acid(letter, coordinates))
            x = x + 1
            coordinates = (x, y)
    def __str__(self):
        string = ''
        for amino_acid in self.sequence:
            string = string + str(amino_acid)
        return string

    def stability(self):
        stability = 0

        #spagetti
        for amino_acid in self.sequence:
            if amino_acid.kind == 'H':
                for amino_acid2 in self.sequence:
                    if (amino_acid2.kind == 'H' and amino_acid != amino_acid2 and
                        abs(self.sequence.index(amino_acid2) - self.sequence.index(amino_acid)) != 1):
                        rest = (amino_acid.coordinates[0] -
                                amino_acid2.coordinates[0],
                                amino_acid.coordinates[1] -
                                amino_acid2.coordinates[1])
                        if abs(rest[0]) == 1 and rest[1] == 0 or abs(rest[1]) == 1 and rest[0] == 0:
                            stability = stability - 1
        return stability / 2

    def turn(self, nodelocation, direction):
        relativelocation = self.sequence[nodelocation].coordinates
        while nodelocation < len(self.sequence) - 1:
            nodelocation = nodelocation + 1
            location = self.sequence[nodelocation].coordinates
            relativex = location[0] - relativelocation[0]
            relativey = location[1] - relativelocation[1]
            temp = relativex
            if direction == 'Left':
                relativex = -relativey + relativelocation[0]
                relativey = temp  + relativelocation[1]
            if direction == 'Right':
                relativex = relativey + relativelocation[0]
                relativey = -temp + relativelocation[1]
            self.sequence[nodelocation].coordinates = (relativex, relativey)
        return

    def check_vadility(self):
        for amino_acid in self.sequence:
            for amino_acid2 in self.sequence:
                if amino_acid != amino_acid2:
                    if amino_acid.coordinates == amino_acid2.coordinates:
                        return False
        return True


if __name__ == '__main__':
    molecule = Molecule('HHPHHHPH')
    print(molecule.stability())
