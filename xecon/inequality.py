import numpy as np
from numpy.random import default_rng
from .math import mean_abs_diff_vectorized, mean_abs_diff_partial_vectorized
import matplotlib.pyplot as plt


def lorenz(data):
    """lorentz curve of raw data"""
    data = np.array(data)
    data.sort()
    cumulative_sum = data.cumsum()
    normalized_cumulative_sum = cumulative_sum / cumulative_sum[-1]
    data_proportion = (np.arange(len(data)) + 1) / (len(data))
    # normalized_cumulative_sum = np.insert(normalized_cumulative_sum, 0, 0)
    # data_proportion = np.insert(data_proportion, 0, 0)
    return data_proportion, normalized_cumulative_sum


def gini(data, method='def'):
    """:param
        data: one dimensional list or numpy.ndarray of sample data in
        method: mathematically equivalent method of gini coefficient calculation,
                allow values are ['def', 'trapz', 'mad']
        :return
        return gini coefficient of input sample data
    """
    if method == 'trapz':
        # trapezoidal method
        return _gini_trapz(data)
    elif method == 'mad':
        # mean of different method
        return _gini_mean_abs_diff(data)
    elif method == 'def':
        # definition method
        return _gini_def(data)
    else:
        raise ValueError("method allowed values are ['def', 'trapz', 'mad']")


def _gini_def(data):
    """calculation by definition"""
    f, l = lorenz(data)
    g = 2 * np.mean(f - l)
    return g


def _gini_trapz(data):
    """calculation by trapezoidal method"""
    f, l = lorenz(data)
    f = np.insert(f, 0, 0)
    l = np.insert(l, 0, 0)
    g = 2 * np.trapz(f-l, f)
    return g


def _gini_mean_abs_diff(data):
    """calculation by mean of difference method"""
    data = np.array(data)
    n = len(data)
    # g = mean_abs_diff(data)/np.mean(data)/2
    if n <= 10**4:
        g = mean_abs_diff_vectorized(data)
    else:
        g = mean_abs_diff_partial_vectorized(data)
    g = g / (np.mean(data) * 2)
    return g


def _gini_deviate_from_mean(data):
    """another mathematically equivalent mean of gini coefficient calculation"""
    data = np.array(data)
    data.sort()
    n = len(data)
    mean = np.mean(data)
    d1 = 1 - data/mean
    cd1 = np.cumsum(d1)
    g = 2 * np.sum(cd1) / (n**2)
    return g


def plot_lorenz(data, line_of_equality=True, ax=None):
    # Prepare axis
    if ax is None:
        ax = plt.gca()

    data_proportion, normalized_cumulative_sum = lorenz(data)
    data_proportion = np.append(0, data_proportion)
    normalized_cumulative_sum = np.append(0, normalized_cumulative_sum)
    if line_of_equality:
        # line of equality
        ax.plot([0, 1], 'gray')
    ax.plot(data_proportion, normalized_cumulative_sum)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_aspect('equal')
    ax.set_title('Lorentz Curve')
    ax.set_xlabel('Proportion of Data')
    ax.set_ylabel('Normalized Cumulative Sum')


def plot_hist(data, ax=None, **kwargs):
    if ax is None:
        ax = plt.gca()
    ax.hist(data, density=True, **kwargs)
    ax.set_xlabel('Measurable')
    # ax.set_aspect('equal')
    ax.set_ylabel('Proportion of Population')
    ax.set_title("Distribution of Measurable")


def plot_hist_lorenz(data):
    fig, ax = plt.subplots(1, 2)
    plot_hist(data, ax[0], bins=np.arange(10))
    ax[0].set_xticks(np.arange(10))
    plot_lorenz(data, ax=ax[1])
    fig.tight_layout()
    fig.set_size_inches(10.2, 4.8)
    return fig, ax

