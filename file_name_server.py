import string


def get_file_name(bm, dimK, dimV, kernel, sort, job, sddmm_alg, precision, mem):
    # Select the kernel to profile
    if kernel == 'wmma':
        suffix = '_wmma'
    elif kernel == 'cuda':
        suffix = '_cuda'
    elif kernel == 'sputnik':
        suffix = '_sputnik'
    elif kernel == 'cusparse':
        suffix = '_cusparse'
    elif kernel == 'bell':
        suffix = '_blocked_ell'
    else:
        suffix = '_dense'

    # Select the precision
    if precision == 'half':
        suffix += '_half'
    else:
        suffix += '_single'

    if sort:
        suffix += '_sort'

    # If the job is SpMM
    if job == 'spmm':
        if mem:
            output_file = './csv/mem/spmm/%s_k%d_v%d.csv' % (bm.replace('/raid/datasets/', '').replace('.smtx', '') + suffix, dimK, dimV)
        else:
            output_file = './csv/spmm/%s_k%d_v%d.csv' % (bm.replace('/raid/datasets/', '').replace('.smtx', '') + suffix, dimK, dimV)
    # Else if the job is SDDMM
    else:
        if kernel == 'wmma':
            suffix += '_%s' % sddmm_alg
        if mem:
            output_file = './csv/mem/sddmm/%s_k%d_v%d.csv' % (bm.replace('/raid/datasets/', '').replace('.smtx', '') + suffix, dimK, dimV)
        else:
            output_file = './csv/sddmm/%s_k%d_v%d.csv' % (bm.replace('/raid/datasets/', '').replace('.smtx', '') + suffix, dimK, dimV)
    
    return output_file