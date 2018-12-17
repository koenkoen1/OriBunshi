def spiralfold(molecule):
    """
    Alters a provided molecule object to a spiral-like shape
    """
    i = 1
    length = len(molecule.sequence)
    while i < length - 1:
        while molecule.check_validity():
            molecule.turn(i, "Right")
        molecule.turn(i, "Left")
        i += 1
