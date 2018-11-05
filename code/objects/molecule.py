from amino_acid import Amino_Acid

class Molecule(object):

    # init function
    def __init__(self, sequence):
        self.sequence = []
        coordinates = x, y = (0, 0)

        # produces a list of amino acids with coordinates (0, 0), (0, 1) etc
        for letter in sequence:
            self.sequence.append(Amino_Acid(letter, coordinates))
            y = y + 1
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
                    if amino_acid2.kind == 'H':
                        if amino_acid != amino_acid2:
                            rest = (amino_acid.coordinates[0] - amino_acid2.coordinates[0], amino_acid.coordinates[1] - amino_acid2.coordinates[1])
                            if abs(rest[0]) == 1 or abs(rest[1]) == 1:
                                stability = stability - 1
        return stability

if __name__ == '__main__':
    molecule = Molecule('HHPHHHPH')
    print(molecule.stability())
