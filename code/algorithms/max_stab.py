def spiralfold(molecule, length):
    """
    folds protein into spiral form
    """
    i = 1
    j = 1
    while i < length:
        molecule.turn(i, "Right")
        i += j
        if i > length:
            break

        molecule.turn(i, "Right")
        j += 1
        i += j
