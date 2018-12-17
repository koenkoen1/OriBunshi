directions = ["Left", "Right"]

def climb(molecule):
    """
    A maximum ascent hillclimber algorithm. Tests all configurations at a
    distance of 1 and 2 from the current object with the turn function.
    """
    while turn(1, molecule) or turn(2, molecule):
        continue

def turn(turns, molecule):
    """
    Tests all configurations a certain amount of turns away from current object.
    Alters the object to the best solution found.
    """
    length = len(molecule.sequence)
    route = False
    currentstability = molecule.stability()

    # iterates over every amino_acid object except the first and last
    for i in range(1, length - 1):
        # tries turning in both directions
        for j in range(2):
            # makes specified amount of turns
            for turn in range(turns):
                molecule.turn(i + turn, directions[j])

            # checks if new configuration is an improvement, record it if it is
            if (molecule.check_vadility() and
                molecule.stability() < currentstability):
                currentstability = molecule.stability()
                route = [i, directions[j]]

            # undoes turning
            for turn in range(turns):
                    molecule.turn(i + turn, directions[j - 1])

    # permanently applies best configuration on the molecule
    if route:
        molecule.turn(route[0], route[1])
        molecule.turn(route[0] + 1, route[1])
        return True

    return False
