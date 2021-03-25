import numpy as np
import matplotlib.pyplot as plt


dense_spmm = {
    'fma_pipe_util': 80.44,
    'L1_miss_sector': 3717631,
    'total_inst': 26123039,
    'fma_inst': 17104896,
    'iadd3_inst': 1607680,
}

dense_hspmm = {
    'fma_pipe_util': 0.06,
    'tensor_pipe_util': 14.60,
    'L1_miss_sector': 853632,
    'total_inst': 2010624,
    'hmma_inst': 1048576,
    'iadd3_inst': 240640,
}

sputnik_spmm = {
    'fma_pipe_util': 13.04,
    'L1_miss_sector': 3477300,
    'total_inst': 3260604,
    'fma_inst': 1778048,
    'iadd3_inst': 273940,
}

sputnik_hspmm = {
    'fma_pipe_util': 23.33,
    'fp15_pipe_util': 22.80,
    'L1_miss_sector': 2093942,
    'total_inst': 5565864,
    'fma_inst': 1848064,
    'hadd2_inst': 2079072,
    'iadd3_inst': 262700,
}

fig, ax = plt.subplots(1, 3, figsize=(5, 3))#, tight_layout=True)

l1_miss_sectors_s = [dense_spmm['L1_miss_sector'], sputnik_spmm['L1_miss_sector']]
l1_miss_sectors_h = [dense_hspmm['L1_miss_sector'], sputnik_hspmm['L1_miss_sector']]
memory_labels = ['GeMM', 'SpMM']
x = np.arange(len(memory_labels)) * 0.5
width = 0.2
ax[0].bar(x - width/2, l1_miss_sectors_s, width, label='Single', color='steelblue')
ax[0].bar(x + width/2, l1_miss_sectors_h, width, label='Half', color='lightcoral')
ax[0].set_ylabel('L1$ Missed Sectors')
ax[0].set_xticks(x)
ax[0].set_xticklabels(memory_labels)
# ax[0].legend()
# ax[0].grid(True)

pipeline_s = [dense_spmm['fma_pipe_util'], sputnik_spmm['fma_pipe_util']]
pipeline_h = [dense_hspmm['tensor_pipe_util'], sputnik_hspmm['fma_pipe_util']]
ax[1].bar(x - width/2, pipeline_s, width, label='Single', color='steelblue')
ax[1].bar(x + width/2, pipeline_h, width, label='Half', color='lightcoral')
ax[1].set_ylabel('Max Compute Pipe Utilization (%)')
ax[1].set_xticks(x)
ax[1].set_xticklabels(memory_labels)
ax[1].legend(ncol=2, bbox_to_anchor = (0,0.2,1,1), loc = 'upper center')
# ax[1].grid(True)

inst_fma_s = [dense_spmm['fma_inst'] + dense_spmm['iadd3_inst'], sputnik_spmm['fma_inst'] + sputnik_spmm['iadd3_inst']]
inst_others_s = [dense_spmm['total_inst'] - dense_spmm['fma_inst'] - dense_spmm['iadd3_inst'], sputnik_spmm['total_inst'] - sputnik_spmm['fma_inst'] - sputnik_spmm['iadd3_inst']]
inst_fma_h = [dense_hspmm['hmma_inst'] + dense_hspmm['iadd3_inst'], sputnik_hspmm['fma_inst'] + sputnik_hspmm['hadd2_inst'] + sputnik_hspmm['iadd3_inst']]
inst_others_h = [dense_hspmm['total_inst'] - dense_hspmm['hmma_inst'] - dense_hspmm['iadd3_inst'], sputnik_hspmm['total_inst'] - sputnik_hspmm['fma_inst'] - sputnik_hspmm['hadd2_inst'] - sputnik_hspmm['iadd3_inst']]

ax[2].bar(x-width/2, inst_fma_s, width, label='Single', color='steelblue')
ax[2].bar(x-width/2, inst_others_s, width, bottom=inst_fma_s, color='lightgray')
ax[2].bar(x+width/2, inst_fma_h, width, label='Half', color='lightcoral')
ax[2].bar(x+width/2, inst_others_h, width, bottom=inst_fma_h, color='lightgray')
ax[2].set_ylabel('Instruction Executed')
ax[2].set_xticks(x)
ax[2].set_xticklabels(memory_labels)
# ax[2].legend()
# ax[2].grid(True)
plt.subplots_adjust(wspace=0.6)
fig.savefig('./mmspmm.pdf', bbox_inches='tight')