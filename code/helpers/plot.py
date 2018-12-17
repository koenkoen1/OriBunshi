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
            logy=True, color='orange')

    # layout
    plt.suptitle(title, fontsize=13, fontweight='bold')
    plt.title(df.columns.values[3], fontsize=10)
    plt.ylabel("Solutions Found")
    plt.xlabel("Stability")

    filename = f"{filepath}.png"
    plt.savefig(filename)
    plt.clf()


def line(name, df, filepath):
    """
    Plots line subplots of both columns of given data frame, saves it at given
    filepath location.
    """

    # make annaling plot
    if name == 'annealing':
        axes = df.plot(x='function evaluations', y=['temperature', 'stability'],
                       subplots=True, sharex=True, figsize=(8, 6), legend=False)
        axes[0].set_ylabel("Temperature")
        axes[1].set_ylabel("Stability")

        # layout
        plt.suptitle("Simulated Annealing", fontsize=13, fontweight='bold')
        plt.xlabel("Function evaluations")

        # show molecule sequence
        plt.title(df.columns.values[4], fontsize=10)

    # make population based plot
    else:
        df.plot(x='function evaluations', y='stability', figsize=(8, 6),
                legend=False)

        # layout
        plt.suptitle("Population based", fontsize=13, fontweight='bold')
        plt.xlabel("Function evaluations")
        plt.ylabel("Stability")

        # show molecule sequence
        plt.title(df.columns.values[3], fontsize=10)

    # save plot
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

    if name == 'annealing' or name == 'population':
        line(name, df, filepath[:-4])
    elif name == 'randomsample':
        df = remove_end_zero(df)
        bar(df, filepath[:-4], "Random Samples")
