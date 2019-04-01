import simulate_fast as simulate


def nsamples(n):
    return sum([simulate.sample(100, 50)==100 for _ in range(n)])/n


if __name__ == '__main__':
    print(nsamples(10000))
