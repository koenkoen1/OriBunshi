class Amino_Acid(object):
    def __init__(self, kind, coordinates):
        self.kind = kind
        self.coordinates = coordinates

    def __str__(self):
        return 'Kind: ' + str(self.kind) + 'coordinates: ' + str(self.coordinates)

    def move(self, coordinates):
        self.coordinates = coordinates
