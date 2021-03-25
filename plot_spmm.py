import numpy as np
import matplotlib.pyplot as plt
import argparse
import csv
import os

# Args
parser = argparse.ArgumentParser(description='plot the acceleration')

parser.add_argument('--start', type=int, default=0, help='the starting benchmark to run')
parser.add_argument('--end', type=int, default=1130, help='the ending benchmark to run')
parser.add_argument('--dimK', type=int, default=-1, help='the dimension k of the benchmark')
parser.add_argument('--sort', action='store_true', help='sort the csr list')

args = parser.parse_args()

bm_list = open('/raid/datasets/dlmc/rn50_matrices.txt', 'r')
lines = bm_list.readlines()

# function that collects the result
def extract_duration_ncu(file):
    if os.path.exists(file):
        with open(file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            unit = 'unknown'

            for row in csvreader:
                if len(row) >= 3 and "Duration" in row[-4]:
                    unit = row[-3]
                    try:
                        dur = float(row[-2])
                        if unit == 'second':
                            dur *= 1000
                        elif unit == 'usecond':
                            dur /= 1000
                        elif unit == 'nsecond':
                            dur /= 1e+6
                        else:
                            print('unknown unit')
                        return dur
                    except:
                        print(file)
                        return -1.0
                    
            print("cannot find duration")
    else:
        print('file %s does not exist' % file)

def extract_duration_set(v, kernel, list_):
    if kernel == 'wmma':
        suffix = '_wmma'
    elif kernel == 'cuda':
        suffix = '_cuda'
    else:
        suffix = '_dense'
    
    suffix_dense = '_dense_sort'

    if args.sort:
        suffix += '_sort'
        
    for i in np.arange(args.start, args.end):
        benchmark = lines[i][:-6]
        file_kernel = './csv/dlmc/%s_k%d_v%d.csv' % (benchmark + suffix, args.dimK, v)
        file_dense = './csv/dlmc/%s_k%d_v%d.csv' % (benchmark + suffix_dense, args.dimK, v)
        dur_kernel = extract_duration_ncu(file_kernel)
        dur_dense = extract_duration_ncu(file_dense)
        if dur_kernel > 0:
            dur_kernel = dur_dense / dur_kernel
            if ('0.5' in benchmark):
                list_[0].append(dur_kernel)
            elif('0.7' in benchmark):
                list_[1].append(dur_kernel)
            elif('0.8' in benchmark):
                list_[2].append(dur_kernel)
            elif('0.95' in benchmark):
                list_[4].append(dur_kernel)
            elif('0.98' in benchmark):
                list_[5].append(dur_kernel)
            elif('0.9' in benchmark):
                list_[3].append(dur_kernel)
            else:
                print("undefined sparsity")


# dense_v1 = [[], [], [], [], [], []]
cuda_v1 = [[], [], [], [], [], []]
extract_duration_set(1, 'cuda', cuda_v1)

# dense_v2 = [[], [], [], [], [], []]
cuda_v2 = [[], [], [], [], [], []]
wmma_v2 = [[], [], [], [], [], []]

extract_duration_set(2, 'cuda', cuda_v2)
extract_duration_set(2, 'wmma', wmma_v2)

# dense_v4 = [[], [], [], [], [], []]
cuda_v4 = [[], [], [], [], [], []]
wmma_v4 = [[], [], [], [], [], []]

extract_duration_set(4, 'cuda', cuda_v4)
extract_duration_set(4, 'wmma', wmma_v4)

# dense_v8 = [[], [], [], [], [], []]
cuda_v8 = [[], [], [], [], [], []]
wmma_v8 = [[], [], [], [], [], []]

extract_duration_set(8, 'cuda', cuda_v8)
extract_duration_set(8, 'wmma', wmma_v8)

def plot(ax, color, bias, data, label='nn'):
    return ax.boxplot(data, positions=[1 + bias, 2 + bias, 3 + bias, 4 + bias, 5 + bias, 6 + bias], notch=True, patch_artist=True,
        boxprops=dict(facecolor=color),
        capprops=dict(color=color),
        whiskerprops=dict(color=color),
        flierprops=dict(color=color, markeredgecolor=color),
        medianprops=dict(color='black'),
        widths=0.35)


fig, axs = plt.subplots(2, 2)

axs[0, 0].plot([0.5, 6.5],[1, 1], color='purple')
c1_p = plot(axs[0, 0], 'steelblue', 0, cuda_v1, 'cuda')

axs[0, 0].set_xticks([1, 2, 3, 4, 5, 6])
axs[0, 0].set_xticklabels([0.5, 0.7, 0.8, 0.9, 0.95, 0.98])
axs[0, 0].legend([c1_p["boxes"][0]], ['cuda'], loc='upper left')
axs[0, 0].set_ylabel('Speedup over cublasHgemm')
axs[0, 0].set_title('V=1')

axs[0, 1].plot([0.5, 7],[1, 1], color='purple')
c2_p = plot(axs[0, 1], 'steelblue', 0, cuda_v2, 'cuda')
w2_p = plot(axs[0, 1], 'lightcoral', 0.5, wmma_v2, 'wmma')

axs[0, 1].legend([c2_p["boxes"][0], w2_p["boxes"][0]], ['cuda', 'mma'], loc='upper left')
axs[0, 1].set_xticks([1, 2, 3, 4, 5, 6])
axs[0, 1].set_xticklabels([0.5, 0.7, 0.8, 0.9, 0.95, 0.98])
axs[0, 1].set_title('V=2')

axs[1, 0].plot([0.5, 7],[1, 1], color='purple')
c4_p = plot(axs[1, 0], 'steelblue', 0, cuda_v4, 'cuda')
w4_p = plot(axs[1, 0], 'lightcoral', 0.5, wmma_v4, 'wmma')

axs[1, 0].legend([c4_p["boxes"][0], w4_p["boxes"][0]], ['cuda', 'mma'], loc='upper left')
axs[1, 0].set_xticks([1, 2, 3, 4, 5, 6])
axs[1, 0].set_xticklabels([0.5, 0.7, 0.8, 0.9, 0.95, 0.98])
axs[1, 0].set_xlabel('Sparsity')
axs[1, 0].set_ylabel('Speedup over cublasHgemm')
axs[1, 0].set_title('V=4')

axs[1, 1].plot([0.5, 7],[1, 1], color='purple')
c8_p =plot(axs[1, 1], 'steelblue', 0, cuda_v8, 'cuda')
w8_p = plot(axs[1, 1], 'lightcoral', 0.5, wmma_v8, 'wmma')

axs[1, 1].legend([c8_p["boxes"][0], w8_p["boxes"][0]], ['cuda', 'mma'], loc='upper left')
axs[1, 1].set_xticks([1, 2, 3, 4, 5, 6])
axs[1, 1].set_xticklabels([0.5, 0.7, 0.8, 0.9, 0.95, 0.98])
axs[1, 1].set_xlabel('Sparsity')
axs[1, 1].set_title('V=8')

plt.subplots_adjust(hspace=0.3)
fig.savefig('./spmm_speedup.pdf', bbox_inches='tight')