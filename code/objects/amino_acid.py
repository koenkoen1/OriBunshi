class Amino_Acid(object):
    def __init__(self, kind, coordinates):
        self.kind = kind
        self.coordinates = coordinates

    def __str__(self):
        return str(self.kind) + str(self.coordinates)

    def move(self, coordinates):
        self.coordinates = coordinates
