import os
import csv
from plot import plot


def filepath(name):
    """
    Outputs a filepath for saving output data.
    """

    # save output in results directory
    path = "./results/"

    # increment filename with 1 wrt last file, to not overwrite it
    i = 0
    while os.path.exists(f"{path}{name}{i}.csv"):
        i += 1

    filepath = f"{path}{name}{i}.csv"

    return filepath


def write_csv(name, header, data):
    """
    Output a CSV file with given data.
    """
    path = filepath(name)
    with open(path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)

        # write header
        writer.writerow(header)

        # iterate over and write movies
        for iteration in data:
            writer.writerow(iteration)

    plot(name, path)
