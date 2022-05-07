import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from matplotlib import cm
from matplotlib.font_manager import FontProperties

# create mock income data
seed = 10
rng = default_rng(seed)
std = 1
mean = 1
n = 5000
# income_data = rng.exponential(1, n)


def lognormal(mean, sigma, n, **kwargs):
    _mean = np.log(mean**2/np.sqrt(mean**2 + sigma**2))
    _sigma = np.sqrt(np.log(1+(sigma/mean)**2))
    return rng.lognormal(_mean, _sigma, n, **kwargs)


income_data = lognormal(mean, std, n)
income_data.sort()


def sample_gen(filename='premade_lognormal_sample.sample', n=100):
    sample = lognormal(mean, std, n)
    with open(f"./{filename}", 'wb') as f:
        pickle.dump(sample, f)


def sample_gen_group(samplenumber_list=(100,)):
    for _ in samplenumber_list:
        sample_gen(f"premade_lognormal_sample_pop{_}.sample", n=_)


def sample_load(filename):
    with open(f"./{filename}", 'rb') as f:
        x = pickle.load(f)
    return x


def group_aggregate_sum(data, n_group):
    """sum of equally separated groups of data"""
    data = np.array(data)
    data.sort()
    q = np.array(np.split(data, n_group))
    group_sum = np.sum(q, axis=1)
    group_bins = (np.arange(len(group_sum))+1)*len(data)/len(group_sum)
    return group_bins, group_sum


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


def plot_lorenz(data, line_of_equality=True, ax=None):
    # Prepare axis
    if ax is None:
        ax = plt.gca()

    data_proportion, normalized_cumulative_sum = lorenz(data)
    ax.plot(data_proportion, normalized_cumulative_sum)
    if line_of_equality:
        # line of equality
        ax.plot([0, 1])
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_aspect('equal')
    ax.set_title('Lorentz Curve')
    ax.set_xlabel('Proportion of Data')
    ax.set_ylabel('Normalized Cumulative Sum')


def gini_trapz(data):
    f, l = lorenz(data)
    f = np.insert(f, 0, 0)
    l = np.insert(l, 0, 0)
    g = 2 * np.trapz(f-l, f)
    return g


def gini_def(data):
    f, l = lorenz(data)
    f = f
    l = l
    n = len(f)
    # g = 2 * np.mean(f-l)*n/(n-1)
    g = 2 * np.mean(f - l)
    # it's 2 times statistic mean for lorentz
    return g


def gini_deviate_from_one(data):
    data = np.array(data)
    data.sort()
    n = len(data)
    mean = np.mean(data)
    d1 = 1 - data/mean
    cd1 = np.cumsum(d1)
    # g = 2 * np.sum(cd1) / (n * (n-1))
    g = 2 * np.sum(cd1) / (n**2)
    return g


def mean_abs_diff_vectorized(data):
    data = np.array(data)
    n = len(data)
    a1, a2 = np.meshgrid(data, data)
    return np.sum(np.abs(a1-a2))/(n*n)


def mean_abs_diff(data):
    data = np.array(data)
    n = len(data)
    result = 0
    for _i in data:
        for _j in data:
            result += np.abs(_i-_j)
    return result/(n*n)


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


def gini_mean_abs_diff(data):
    data = np.array(data)
    n = len(data)
    # g = mean_abs_diff(data)/np.mean(data)/2
    if n <= 10**4:
        g = mean_abs_diff_vectorized(data)
    else:
        g = mean_abs_diff_partial_vectorized(data)
    g = g /(np.mean(data) * 2)
    return g


# granular test
def granular_effect():
    ax = plt.gca()
    g = np.array([1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 500, 1000, 1250, 2500, 5000])
    gini_granular = []
    for _ in g:
        x, y = group_aggregate_sum(income_data, _)
        gini_granular.append(gini_def(y))

    gini_granular = np.array(gini_granular)
    gini_real = gini_def(income_data)
    ax.plot(g, gini_granular)
    ax.plot(g, gini_real * np.ones_like(g), '--', color='red')
    ax = plt.gca()
    ax.set_xscale('log')
    ax.grid(which='both', axis='both')
    ax.set_xlim(g.min(), g.max())
    ax.set_ylim(gini_granular.min(), np.ceil(gini_granular.max()*10)/10)
    ax.set_title('Granular Effect (population n = 5000)')
    ax.set_ylabel('Gini Coefficient')
    ax.set_xlabel('Number of Group')
    ax.text(1, gini_real, "Population's Gini Coefficient")


# def decile_error(population_number, gini_method):
#     sample = lognormal(mean, std, population_number)
#     x, y = group_aggregate_sum(sample, 10)
#     gini_real = gini_method(sample)
#     gini_dec = gini_method(y)
#     return gini_real, gini_dec

def decile_error(sample, gini_method):
    x, y = group_aggregate_sum(sample, 10)
    gini_real = gini_method(sample)
    gini_dec = gini_method(y)
    return gini_real, gini_dec


def decile_error_plot(pop_max=10**6, gini_method=gini_def, ax=None):
    g = np.arange(8) + 2
    population_number = 10**g
    pop_plot = []
    r = []
    d = []
    for _ in population_number:
        pop = _
        if pop > pop_max:
            break
        sample = sample_load(f"premade_lognormal_sample_pop{_}.sample")
        pop_plot.append(pop)
        print(f"processing simulate population = {pop}")
        _r, _d = decile_error(sample, gini_method)
        r.append(_r)
        d.append(_d)
    r = np.array(r)
    d = np.array(d)
    if ax is None:
        ax = plt.gca()
    ax.plot(pop_plot, r)
    ax.plot(pop_plot, d)
    ax.legend(["Sample's", "Decile's"])
    ax.set_xlabel('Number of Sample')
    ax.set_ylabel('Gini Coefficient')
    ax.set_xscale('log')
    return r, d


# plt.xticks(g[:4], g[:4])
# yt = gini_granular[:4].copy()
# yt.insert(0, gini_real)
# yt.sort()
# plt.yticks(yt, yt)

# plt.plot([0, 1])
# plt.plot(*lorentz(income_data))
# x = group_aggregate_sum(income_data, 10)
# plt.plot(*lorentz(x[1]))
# plot_lorenz(income_data)
#########################
# fig_1 = plt.figure()
# ax = plt.gca()
# r, d = decile_error_plot(pop_max=10**8, ax=ax)
# ax.set_title("Calculation of Decile Grouping of Sample\n"
#              "Definition Method\n"
#              "(Lognormal Distribution)")
# ax.set_xlim(50.11872336272722, 199526231.49688828)
# ax.set_ylim(0.4288755689771227, 0.4740415525330986)
# fig_1.tight_layout()
# # plt.show()
#
# print('saving def figure')
# fig_1.savefig(fname='def_gini_decile_errorvspop.png', dpi=600)
#
# print('saving def data')
# with open('./decile_error_def.gini', 'wb') as f:
#     pickle.dump([r, d], f)
#
# print('finished definition')
#
# fig_2 = plt.figure()
# ax = plt.gca()
# r_2, d_2 = decile_error_plot(pop_max=10**6, gini_method=gini_mean_abs_diff, ax=ax)
# ax.set_title("Calculation of Decile Grouping of Sample\n"
#              "Mean of Absolute Differences Method\n"
#              "(Lognormal Distribution)")
# ax.set_xlim(50.11872336272722, 199526231.49688828)
# ax.set_ylim(0.4288755689771227, 0.4740415525330986)
# fig_2.tight_layout()
# # plt.show()
# print('saving mad figure')
# fig_2.savefig(fname='mad_gini_decile_errorvspop.png', dpi=600)
# # r_2, d_2 = decile_error_plot(pop_max=10**5)
# print('saving mad data')
# with open('./decile_error_mad.gini', 'wb') as f:
#     pickle.dump([r_2, d_2], f)
# print('finished mean of different')
###########################
# my_cmap = cm.turbo(range(256))

def gen_example(std=0.7):
    x = np.arange(10) + 1
    h = lognormal(1, std, 10)
    return x, h


def cumsum_visual(samples, cmap=cm.turbo):
    cmap = cmap(range(256))
    x, h = samples
    if h.max()-h.min() > 0:
        c = 255*(h-h.min())/(h.max()-h.min())
    else:
        c = 127*np.ones_like(h)
    c = np.asarray(c, dtype=int)
    fig1 = plt.figure()
    plt.xticks(x)
    plt.ylim([0, h.sum()+h.sum()*0.1])
    plt.xlabel('คนที่', fontfamily='TH Sarabun New', fontsize=20)
    plt.ylabel('รายได้', fontfamily='TH Sarabun New', fontsize=20)
    plt.title('รายได้ของตัวอย่าง 10 คน', fontfamily='TH Sarabun New', fontsize=20)
    for _ in np.arange(10):
        plt.bar(x[_], h[_], color=cmap[c[_]])
    fig1.savefig('./lorenz_exp/samples_income.png')

    h = np.sort(h)
    c = np.sort(c)
    fig2 = plt.figure()
    plt.xticks(x)
    plt.ylim([0, h.sum() + h.sum() * 0.1])
    plt.xlabel('คนที่', fontfamily='TH Sarabun New', fontsize=20)
    plt.ylabel('รายได้', fontfamily='TH Sarabun New', fontsize=20)
    plt.title('รายได้ของตัวอย่าง 10 คน เรียงจากน้อยไปหามาก', fontfamily='TH Sarabun New', fontsize=20)
    for _ in np.arange(10):
        plt.bar(x[_], h[_], color=cmap[c[_]])
    fig2.savefig('./lorenz_exp/samples_income_sorted.png')

    fig3, axes = plt.subplots(1, 2)
    fig3.set_size_inches(12.8, 6.4)
    ax = axes[1]
    ax.set_xticks(np.append(0, x))
    ax.set_ylim([0, np.sum(h)+np.sum(h)*0.1])
    ax.set_xlabel('ผลรวมเชิงสะสมของตัวอย่าง', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_ylabel('ผลรวมเชิงสะสมของรายได้', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_title('ผลรวมเชิงสะสมของของรายได้เทียบกับของตัวอย่าง', fontfamily='TH Sarabun New', fontsize=20)
    ax.bar(0, 0)
    ax.grid(axis='y')
    ax = axes[0]
    ax.set_xticks(x)
    ax.set_ylim([0, h.sum() + h.sum() * 0.1])
    ax.set_xlabel('คนที่', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_ylabel('รายได้', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_title('รายได้ของตัวอย่าง 10 คน เรียงจากน้อยไปหามาก', fontfamily='TH Sarabun New', fontsize=20)
    ax.grid(axis='y')
    for _ in np.arange(10):
        ax.bar(x[_], h[_], color=cmap[c[_]])
    fig3.tight_layout()
    for i in range(10):
        cumulative = 0
        for _ in np.arange(10):
            axes[0].bar(x[_], h[_], color=cmap[c[_]])
        for j in range(i+1):
            axes[0].bar(j+1, h[j], color='yellow')
            axes[1].bar(i+1, h[j], color=cmap[c[j]], bottom=cumulative)
            cumulative += h[j]
            fig3.savefig(f'./lorenz_exp/cumsum_animation{i}{j}.png')
            # plt.draw()
            # plt.pause(0.1)

    fig4 = plt.figure()
    ax = plt.axes()
    h = h/h.sum()
    ax.set_xlabel('ผลรวมเชิงสะสมของสัดส่วนตัวอย่าง', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_ylabel('ผลรวมเชิงสะสมของสัดส่วนรายได้', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_title('ผลรวมเชิงสะสมของของสัดส่วนรายได้เทียบกับของสัดส่วนตัวอย่าง', fontfamily='TH Sarabun New', fontsize=20)
    ax.grid(axis='y')
    x_labels = x/x[-1]
    ax.bar(0, 0)
    ax.bar(x, h[0] * np.ones_like(x), color=cmap[c[0]])
    cumulative = h[0]
    ax.set_xticks(np.append(0, x))
    ax.set_xticklabels(np.append(0, x_labels))
    for _ in np.arange(9)+1:
        ax.bar(x[_:], h[_]*np.ones_like(x[_:]), bottom=cumulative*np.ones_like(x[_:]), color=cmap[c[_]])
        cumulative += h[_]
    fig4.savefig('./lorenz_exp/cumsum_proportion.png')
    f, l = lorenz(h)
    f_scale = np.arange(11)
    f = np.append(0, f)
    l = np.append(0, l)
    ax.plot(f_scale, l, marker='o')
    fig4.savefig('./lorenz_exp/cumsum_proportion_with_lorenze.png')
    fig5 = plt.figure()
    ax = plt.axes()
    ax.set_xlabel('ผลรวมเชิงสะสมของสัดส่วนตัวอย่าง', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_ylabel('ผลรวมเชิงสะสมของสัดส่วนรายได้', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_title('โค้งลอเลนซ์', fontfamily='TH Sarabun New', fontsize=20)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.plot(f, l, marker='o')
    fig5.savefig('./lorenz_exp/lorenze_curve.png')


# plt.fill_between(l2, l2, l1, color='red', alpha=0.2)
# plt.plot(l2, l1)
# plt.plot(l2, l2, color='gray')
# plt.xlabel('ผลรวมเชิงสะสมของสัดส่วนตัวอย่าง', fontfamily='TH Sarabun New', fontsize=20)
# plt.ylabel('ผลรวมเชิงสะสมของสัดส่วนรายได้', fontfamily='TH Sarabun New', fontsize=20)
# plt.title('พื้นที่ระหว่างเส้นแห่งความเท่าเทียมกับโค้งลอเลนซ์', fontfamily='TH Sarabun New', fontsize=20)
# ax = plt.gca()
# ax.set_aspect('equal')
# ax.set_xlim([0,1])
# ax.set_ylim([0,1])
# plt.fill_between(l2, l3, l2, color='red', alpha=0.2)
# plt.plot(l2, l3)
# plt.title('พื้นที่ที่เท่ากับสัมประสิทธิ์จีนี่', fontfamily='TH Sarabun New', fontsize=20)