import numpy as np
import matplotlib.pyplot as plt


def plot_data(X, y, ax):
    pos = y.flatten() == 1
    neg = y.flatten() == 0

    ax.scatter(
        X[pos, 0],
        X[pos, 1],
        marker='+',
        c='k',
        s=80,
        linewidths=2,
        label='y = 1'
    )

    ax.scatter(
        X[neg, 0],
        X[neg, 1],
        marker='o',
        c='k',
        s=50,
        label='y = 0'
    )