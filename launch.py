import os


"""# For memory
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.5/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.5/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.5/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.5/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.5/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.5/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.7/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.7/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.7/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.7/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.7/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.7/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.8/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.8/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.8/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.8/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.8/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.8/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.9/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.9/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.9/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.9/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.9/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.9/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.95/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.95/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.95/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.95/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.95/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.95/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.98/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.98/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 2 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.98/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.98/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 4 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.98/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel bell --prof --job spmm --precision half --mem'
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm /raid/datasets/dlmc/rn50/magnitude_pruning/0.98/bottleneck_projection_block_group_projection_block_group4.smtx -k 256 -v 8 --kernel wmma --sort --prof --job spmm --precision half --mem'
os.system(cmd)
"""

"""# For Blocked Ell

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 2 --kernel dense --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 4 --kernel dense --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 8 --kernel dense --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 16 --kernel dense --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 2 --kernel bell --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 4 --kernel bell --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 8 --kernel bell --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 16 --kernel bell --job spmm --precision half'
os.system(cmd)
"""


""" For finegrained SDDMM and SpMM
cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --job sddmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel sputnik --job sddmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --job sddmm --precision single'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel sputnik --job sddmm --precision single'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel cusparse --job sddmm --precision single'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --sort --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel sputnik --sort --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel cusparse --sort --job spmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --sort --job spmm --precision single'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel sputnik --sort --job spmm --precision single'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel cusparse --sort --job spmm --precision single'
os.system(cmd)
"""

""" For sddmm no sort
cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --job sddmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel cuda --job sddmm --precision half'
os.system(cmd)

Vs = [2, 4, 8]

for v in Vs:
    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel dense --job sddmm --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel cuda --job sddmm --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --job sddmm --sddmm_alg wmma --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --job sddmm --sddmm_alg mma_reg --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --job sddmm --sddmm_alg mma_shfl --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --job sddmm --sddmm_alg mma_arch --precision half' %v
    os.system(cmd)
"""

""" For sddmm sort
cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --sort --job sddmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel cuda --sort  --job sddmm --precision half'
os.system(cmd)

Vs = [2, 4, 8]

for v in Vs:
    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel dense --sort --job sddmm --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel cuda --sort --job sddmm --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg wmma --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_reg --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_shfl --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_arch --precision half' %v
    os.system(cmd)
"""

"""
# For spmm

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --job spmm --sort --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel sputnik --job spmm --sort --precision half'
os.system(cmd)

Vs = [2, 4, 8]

for v in Vs:
    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel dense --job spmm --sort --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel cuda --job spmm --sort --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --job spmm --sort --precision half' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel bell --job spmm --sort --precision half' %v
    os.system(cmd)
"""


"""
# For spmm on transformer

cmd = 'python3 job_launcher.py --start 0 --end 679 --dimK 256 --dimV 1 --kernel dense --job spmm --sort --precision half --bm transformer'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 679 --dimK 256 --dimV 1 --kernel sputnik --job spmm --sort --precision half --bm transformer'
os.system(cmd)

Vs = [2, 4, 8]

for v in Vs:
    cmd = 'python3 job_launcher.py --start 0 --end 679 --dimK 256 --dimV %d --kernel dense --job spmm --sort --precision half --bm transformer' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 679 --dimK 256 --dimV %d --kernel cuda --job spmm --sort --precision half --bm transformer' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 679 --dimK 256 --dimV %d --kernel wmma --job spmm --sort --precision half --bm transformer' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 679 --dimK 256 --dimV %d --kernel bell --job spmm --sort --precision half --bm transformer' %v
    os.system(cmd)
"""

"""
# For sddmm transformer
cmd = 'python3 job_launcher.py --start 321 --end 679 --dimK 256 --dimV 1 --kernel dense --sort --job sddmm --precision half --bm transformer'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 321 --end 679 --dimK 256 --dimV 1 --kernel cuda --sort  --job sddmm --precision half --bm transformer'
os.system(cmd)

Vs = [2, 4, 8]

for v in Vs:
    cmd = 'python3 job_launcher.py --start 321 --end 679 --dimK 256 --dimV %d --kernel dense --sort --job sddmm --precision half --bm transformer' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 321 --end 679 --dimK 256 --dimV %d --kernel cuda --sort --job sddmm --precision half --bm transformer' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 321 --end 679 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg wmma --precision half --bm transformer' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 321 --end 679 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_reg --precision half --bm transformer' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 321 --end 679 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_shfl --precision half --bm transformer' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 321 --end 679 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_arch --precision half --bm transformer' %v
    os.system(cmd)
"""

"""
# for SpMM kernel under different K

for k in [64, 128, 512]:
    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV 1 --kernel dense --job spmm --sort --precision half' % k
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV 1 --kernel sputnik --job spmm --sort --precision half' % k
    os.system(cmd)

    Vs = [2, 4, 8]

    for v in Vs:
        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel dense --job spmm --sort --precision half' % (k, v)
        os.system(cmd)

        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel cuda --job spmm --sort --precision half' % (k, v)
        os.system(cmd)

        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel wmma --job spmm --sort --precision half' % (k, v)
        os.system(cmd)

        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel bell --job spmm --sort --precision half' % (k, v)
        os.system(cmd)
"""

for k in [64, 128, 512]:
    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV 1 --kernel dense --sort --job sddmm --precision half' % k
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV 1 --kernel cuda --sort  --job sddmm --precision half' % k
    os.system(cmd)

    Vs = [2, 4, 8]

    for v in Vs:
        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel dense --sort --job sddmm --precision half' % (k, v)
        os.system(cmd)

        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel cuda --sort --job sddmm --precision half' % (k, v)
        os.system(cmd)

        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg wmma --precision half' % (k, v)
        os.system(cmd)

        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_reg --precision half' % (k, v)
        os.system(cmd)

        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_shfl --precision half' % (k, v)
        os.system(cmd)

        cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK %d --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_arch --precision half' % (k, v)
        os.system(cmd)