class Amino_Acid(object):
    def __init__(self, kind, coordinates):
        """
        initializes an Amino_Acid object. Saves kind and coordinate attributes.
        """
        self.kind = kind
        self.coordinates = coordinates

    def __str__(self):
        """
        Defines how to print an Amino_Acid object. Returns a string.
        """
        return ('Kind: ' + str(self.kind)
                + ' coordinates: ' + str(self.coordinates))
