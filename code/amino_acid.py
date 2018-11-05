class Amino_Acid(object):
    def __init__(self, kind, coordinates):
        self.kind = kind
        self.coordinates = coordinates

    def move(self, coordinates):
        self.coordinates = coordinates
