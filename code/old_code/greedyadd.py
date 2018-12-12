from amino_acid import Amino_Acid
from molecule import Molecule


def greedyadd(molecule, sequence):
    """
    W.I.P.
    Greedy algorithm to build op molecule amino acid by amino acid.
    """
    seq = sequence

    # add first three amino acids at starting positions
    try:
        acid1 = Amino_Acid(seq[0], (0, 0))
        acid2 = Amino_Acid(seq[1], (1, 0))
        acid3 = Amino_Acid(seq[2], (1, 1))
        molecule.add_acids([acid1, acid2, acid3])
    except ValueError:
        print("Not enough amino acids in sequence for optimization.")

    # skip over first three, already added, amino acids in sequence
    seq = seq[3:]

    x, y = 1, 1

    for letter in seq:

        # create and save amino acid for all possible neighbouring positions
        acid_xplus = Amino_Acid(letter, (x + 1, y))
        acid_yplus = Amino_Acid(letter, (x, y + 1))
        acid_xminus = Amino_Acid(letter, (x - 1, y))
        acid_yminus = Amino_Acid(letter, (x, y - 1))
        possible = [acid_xplus, acid_yplus, acid_xminus, acid_yminus]

        # find and save stabilities that would be if possible acids were added
        stabilities = {}
        for acid in possible:
            if molecule.add_acids([acid]):
                stabilities[acid] = molecule.stability()
                molecule.remove_acids([acid])

        print(stabilities)

        # find amino acid that gives lowest stability
        min_key = min(stabilities, key=stabilities.get)

        # print(min_key)
