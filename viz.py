import random
import simulate

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


if __name__ == '__main__':
    seed = 5
    random.seed(seed)
    num_samples = 1000
    max_tries_options = np.arange(5, 50, 10)
    num_box_options = np.arange(10, 100, 10)
    vsample = np.vectorize(simulate.sample, otypes=[int])

    # dist_items = []
    # for _ in range(num_samples):
    #     for nboxes in [80, 90, 100, 110]:
    #         for ntries in [40, 50, 60, 70]:
    #             sample = simulate.sample(nboxes, ntries)
    #             dist_items.append([nboxes, ntries, sample])

    # df = pd.DataFrame(dist_items, columns=['nboxes', 'ntries', 'npeople'])

    # g = sns.FacetGrid(df, col='nboxes', row='ntries')
    # g.map(plt.hist, 'npeople')
    # plt.show()

    params = np.meshgrid(num_box_options, max_tries_options)
    results = np.array([vsample(*params) for _ in range(num_samples)])
    print(results)
    results_bin = np.sum(results == num_box_options, axis=0) / num_samples

    print(results_bin)
    ax = plt.axes()
    plt.set_cmap('Purples')
    contour = ax.contourf(*params, results_bin)
    ax.set_xlabel('num boxes')
    ax.set_ylabel('max tries allowed')
    ax.set_title('probability of group win')
    plt.colorbar(contour)
    filename = (
    f'{seed}-{num_samples}-{max_tries_options[0]},{max_tries_options[-1]}-{num_box_options[0]},{num_box_options[-1]}.png'
    )
    plt.savefig(filename)
    plt.show()
