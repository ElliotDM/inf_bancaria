import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


graphs_dir = Path('../graphs')


def distribution(x, y, title):
    fig, ax = plt.subplots()
    ax.bar(x, y, color='skyblue', edgecolor='grey')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    plt.title(title)

    distribution_path = graphs_dir / f"{title}.png"
    plt.savefig(distribution_path)
    
    plt.show()


def heatmap(data, title):
    fig, ax = plt.subplots()
    im = ax.pcolor(data, cmap='RdBu')

    row_labels = data.columns
    col_labels = data.index

    ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)

    ax.set_xticklabels(row_labels, minor=False)
    ax.set_yticklabels(col_labels, minor=False)

    plt.xticks(rotation=90)
    fig.colorbar(im)
    plt.title(title)

    heatmap_path = graphs_dir / f"{title}.png"
    plt.savefig(heatmap_path)
    
    plt.show()


def scatter(x, y, title):
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='skyblue', edgecolor='grey')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    plt.title(title)

    distribution_path = graphs_dir / f"{title}.png"
    plt.savefig(distribution_path)
    
    plt.show()
