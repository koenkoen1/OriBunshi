import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(directory)
sys.path.append(os.path.join(parentdir, "objects"))

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def bar(df, filepath, title):
    """
    Plots and shows a bar chrart of data frame.
    """

    # plot bar chart
    df.plot(x='stability', y='solutions found', kind='bar', legend=False,
            color='orange')

    # layout
    plt.suptitle(title, fontsize=13, fontweight='bold')
    plt.title(df.columns.values[3], fontsize=10)
    plt.ylabel("Solutions Found")
    plt.xlabel("Stability")

    filename = f"{filepath}.png"
    plt.savefig(filename)
    plt.clf()


def line(df, filepath):
    """
    Plots line subplots of both columns of given data frame, saves it at given
    filepath location.
    """

    axes = df.plot(y=['temperature', 'stability'], subplots=True, sharex=True,
                   figsize=(8, 6), legend=False)
    axes[0].set_ylabel("Temperature")
    axes[1].set_ylabel("Stability")

    # layout
    plt.suptitle("Simulated Annealing", fontsize=13, fontweight='bold')
    plt.title(df.columns.values[3], fontsize=10)
    plt.xlabel("Iterations")

    filename = f"{filepath}.png"
    plt.savefig(filename)
    plt.clf()


def make_numeric(df):
    """
    Returns data frame with all numbers turned to numeric values.
    """

    # convert numeric column data to numbers
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')

    return df


def remove_end_zero(df):
    """
    Removes all dataframe rows with zero from the last nonzero row down.
    """

    while df.iloc[-1,1] == 0:
        df = df[:-1]

    print(df)

    return df


def plot(name, filepath):
    """
    Determines what type of chart to make and makes that chart.
    """

    input_csv = filepath;
    with open(input_csv, 'r') as infile:

        # create pandas data frame from csv data in infile
        df = pd.read_csv(infile)

        infile.close()

    df = make_numeric(df)

    if name == 'annealing':
        line(df, filepath[:-4])
    elif name == 'randomsample':
        df = remove_end_zero(df)
        bar(df, filepath[:-4], "Random Samples")
