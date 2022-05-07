import numpy as np
from numpy.random import default_rng


def mean_abs_diff(data):
    data = np.array(data)
    n = len(data)
    result = 0
    for _i in data:
        for _j in data:
            result += np.abs(_i-_j)
    return result/(n*n)


def mean_abs_diff_vectorized(data):
    data = np.array(data)
    n = len(data)
    a1, a2 = np.meshgrid(data, data)
    return np.sum(np.abs(a1-a2))/(n*n)


def mean_abs_diff_partial_vectorized(data):
    data = np.array(data)
    split_size = 2*(10**4)
    l = len(data)
    q, r = np.divmod(l, split_size)
    if r > 0:
        a, b = np.split(data, [q*split_size])
        a = np.split(a, q)
        a = np.append(a, b)
    else:
        a = np.split(data, q)
    print(f"chuck size {q}")
    result = 0
    for _i in a:
        for _j in a:
            a1, a2 = np.meshgrid(_i, _j)
            result += np.sum(np.abs(a1-a2))
    return result/(l*l)


def lognormal(mean, sigma, n, seed=None, **kwargs):
    rng = default_rng(seed)
    _mean = np.log(mean**2/np.sqrt(mean**2 + sigma**2))
    _sigma = np.sqrt(np.log(1+(sigma/mean)**2))
    return rng.lognormal(_mean, _sigma, n, **kwargs)


def uniform(value, n):
    return value*np.ones(n)


def two_levels(level1, level2, n, l1_fraction=0.5):
    n1 = int(n*l1_fraction)
    n2 = n-n1
    l1 = uniform(level1, n1)
    l2 = uniform(level2, n2)
    return np.append(l1, l2)
