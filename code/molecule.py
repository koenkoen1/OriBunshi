from amino_acid import Amino_Acid

class Molecule(object):
    def __init__(self, sequence):
        self.sequence = []
        for letter in sequence:
            coordinates = x, y = (0, 0)
            self.sequence.append(Amino_Acid(letter, coordinates))
            y = y + 1
    def __str__(self):
        string = ''
        for amino_acid in self.sequence:
            string = string + str(amino_acid)
        return string

if __name__ == '__main__':
    molecule = Molecule('AAAAA')
    print(molecule)
