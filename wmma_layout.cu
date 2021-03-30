#include <cuda_fp16.h>
#include <stdio.h>
#include <mma.h>
using namespace nvcuda;

__device__ void print_val_h(int threadid, half value, int reg){
    printf("index %.0f, tid: %d, register %d\n", float(value), threadid, reg);
}

__global__ void dummy_wmma(float* d_out){
    // The shared memory that holds the indices
    __shared__ half indices[512];

    // Step 1: write the indices to the shared memory
    for (int i=threadIdx.x; i < 512; i+=blockDim.x){
        indices[i] = half(i);
    }

    __syncthreads();

    // Step 2: declare the fragments
    wmma::fragment<wmma::matrix_a, 8, 32, 16, half, wmma::col_major> a_frag;
    wmma::fragment<wmma::matrix_b, 8, 32, 16, half, wmma::row_major> b_frag;
    wmma::fragment<wmma::accumulator, 8, 32, 16, float> c_frag;

    // Step 3: load the fragments
    wmma::load_matrix_sync(a_frag, indices, 8);

    // #pragma unroll
    // for (int i = 0; i < 16; i++){
    //     print_val_h(threadIdx.x, a_frag.x[i], i);
    // }

    wmma::load_matrix_sync(b_frag, indices, 32);

    #pragma unroll
    for (int i = 0; i < 16; i++){
        print_val_h(threadIdx.x, b_frag.x[i], i);
    }

    wmma::fill_fragment(c_frag, 0.0f);

    // Step 4: do GEMM
    wmma::mma_sync(c_frag, a_frag, b_frag, c_frag);

    // Step 5: stoore the matrix
    wmma::store_matrix_sync(d_out, c_frag, 32, wmma::mem_row_major);
}


int main(void){
    float* d_out;
    cudaMalloc(&d_out, 256 * sizeof(float));

    dummy_wmma<<<1, 32>>>(d_out);

    float* h_out = new float[256];

    cudaMemcpy(h_out, d_out, 256 * sizeof(float), cudaMemcpyDeviceToHost);
    for (int i=0; i < 8; i++){
        for (int j=0; j < 32; j++){
            printf("%.0f ", h_out[i * 32 + j]);
        }
        printf("\n");
    }
}