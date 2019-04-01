import simulate_fast as simulate
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    seed = 5
    simulate.seed_random(seed)
    num_samples = 100
    max_tries_options = np.arange(5, 50, 1)
    num_box_options = np.arange(10, 100, 1)
    vsample = np.vectorize(simulate.sample, otypes=[int])

    params = np.meshgrid(num_box_options, max_tries_options)
    results = np.array([vsample(*params) for _ in range(num_samples)])
    print(results)
    results_bin = np.sum(results == num_box_options, axis=0) / num_samples

    print(results_bin)
    plt.set_cmap("Purples")
    ax = plt.axes()
    contour = ax.contourf(*params, results_bin)
    ax.set_xlabel("num boxes")
    ax.set_ylabel("max tries allowed")
    ax.set_title("probability of group win")
    plt.colorbar(contour)
    filename = f"{seed}-{num_samples}-{max_tries_options[0]},{max_tries_options[-1]}-{num_box_options[0]},{num_box_options[-1]}.png"  # noqa: E501
    plt.savefig(filename)
    # plt.show()
