import os

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --sort --job sddmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel sputnik --sort --job sddmm --precision half'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --sort --job sddmm --precision single'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel sputnik --sort --job sddmm --precision single'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel cusparse --sort --job sddmm --precision single'
os.system(cmd)


""" For finegrained SpMM
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

""" For spmm
cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel dense --sort --job sddmm'
os.system(cmd)

cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV 1 --kernel cuda --sort --job sddmm'
os.system(cmd)

Vs = [2, 4, 8]

for v in Vs:
    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel dense --sort --job sddmm' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel cuda --sort --job sddmm' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg wmma' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_reg' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_shfl' %v
    os.system(cmd)

    cmd = 'python3 job_launcher.py --start 0 --end 323 --dimK 256 --dimV %d --kernel wmma --sort --job sddmm --sddmm_alg mma_arch' %v
    os.system(cmd)
"""