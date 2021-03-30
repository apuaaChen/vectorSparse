# This is a simple script that verifies all the kernels 
import os
import argparse


# Args
parser = argparse.ArgumentParser(description='Verify the functionality of the kernels')
parser.add_argument('--bm', default='/raid/datasets/dlmc/rn50/random_pruning/0.8/bottleneck_2_block_group3_5_1.smtx',
                            help='Path to benchmark')
parser.add_argument('--dimK', '-k', type=int, default=256, help='the dimension K of the benchmark')

args = parser.parse_args()


#
# SpMM
#

# wmma kernels with sorted csr under half precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel wmma --prof --func --job spmm --sort --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel wmma --prof --func --job spmm --sort --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel wmma --prof --func --job spmm --sort --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# wmma kernels with unsorted csr under half precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel wmma --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel wmma --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel wmma --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# cuda kernel with sorted csr under half precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel cuda --prof --func --job spmm --sort --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel cuda --prof --func --job spmm --sort --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel cuda --prof --func --job spmm --sort --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel cuda --prof --func --job spmm --sort --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# cuda kernel with unsorted csr under half precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel cuda --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel cuda --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel cuda --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel cuda --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# Dense kernels under half precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel dense --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel dense --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel dense --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel dense --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# Dense kernels under single precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel dense --prof --func --job spmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel dense --prof --func --job spmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel dense --prof --func --job spmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel dense --prof --func --job spmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)

# Sputnik kernel under half precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel sputnik --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel sputnik --prof --func --job spmm --sort --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# Sputnik kernel under single precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel sputnik --prof --func --job spmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel sputnik --prof --func --job spmm --sort --precision single --print' % (args.bm, args.dimK)
os.system(cmd)

# cusparse kernels
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel cusparse --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel cusparse --prof --func --job spmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)

# bell kernel
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel bell --prof --func --job spmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel bell --prof --func --job spmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)


#
# SDDMM
#

# wmma kernels with unsorted csr under half precision, wmma
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel wmma --sddmm_alg wmma --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel wmma --sddmm_alg wmma --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel wmma --sddmm_alg wmma --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# wmma kernels with unsorted csr under half precision, mma_reg
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel wmma --sddmm_alg mma_reg --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel wmma --sddmm_alg mma_reg --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel wmma --sddmm_alg mma_reg --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# wmma kernels with unsorted csr under half precision, mma_shfl
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel wmma --sddmm_alg mma_shfl --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel wmma --sddmm_alg mma_shfl --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel wmma --sddmm_alg mma_shfl --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# cuda kernel with unsorted csr under half precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel cuda --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel cuda --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel cuda --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel cuda --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# Dense kernels under half precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel dense --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel dense --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel dense --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel dense --prof --func --job sddmm --precision half --print' % (args.bm, args.dimK)
os.system(cmd)

# Dense kernels under single precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel dense --prof --func --job sddmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 2 --kernel dense --prof --func --job sddmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 4 --kernel dense --prof --func --job sddmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 8 --kernel dense --prof --func --job sddmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)

# Sputnik kernel under single precision
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel sputnik --prof --func --job sddmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)

# cusparse kernels
cmd = 'python3 ncu_profile.py --bm %s -k %d -v 1 --kernel cusparse --prof --func --job sddmm --precision single --print' % (args.bm, args.dimK)
os.system(cmd)
