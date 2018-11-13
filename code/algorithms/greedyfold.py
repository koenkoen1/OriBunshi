def spiralfold(molecule, length):
    """
    folds protein into spiral form
    """
    i = 1
    while i < length:
        molecule.turn(i, "Right")
        if not molecule.check_vadility():
            molecule.turn(i, "Left")
        i += 1
