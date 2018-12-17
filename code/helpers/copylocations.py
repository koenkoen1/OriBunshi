def copylocations(molecule1, molecule2):
    """
    Copies coordinates of the amino acids of one molecule to another molecule.
    This function is used for resetting the molecule to the backup or for
    updating the backup to a new configuration.
    """
    for index, amino_acid in enumerate(molecule2.acids):
        molecule1.acids[index].coordinates = amino_acid.coordinates
