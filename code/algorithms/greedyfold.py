def spiralfold(molecule, length):
    """
    Requires the molecule object and the length of the amino acid sequence.
    Folds protein into spiral-like form. Returns folded molecule.
    """
    i = 1
    while i < length:
        molecule.turn(i, "Right")
        if not molecule.check_vadility():
            molecule.turn(i, "Left")
        i += 1
