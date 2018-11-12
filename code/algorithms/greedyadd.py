from molecule import Molecule


def greedyadd(sequence):
    """
    Greedy algorithm to build op molecule amino acid by amino acid.
    """
    seq = sequence

    # set first three amino acids in starting positions
    try:
        molecule.add_acids({seq[0]: (0,0), seq[1]: (1,0), seq[2]: (1,1)})
    except ValueError:
        print("Not enough amino acids in sequence for optimization.")

    seq = seq[3:]

    for letter in seq:
        
        molecule.stability()
