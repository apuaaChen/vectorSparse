#include <cuda_profiler_api.h>
#include <cuda_runtime.h>
#include <stdio.h>
#define TOTAL_COL 20480


__global__ void copy_128B(
    const float* __restrict__ d_in,
    float* __restrict__ d_out,
    size_t total_columns
){
    int row = blockIdx.x;
    int col = blockIdx.y * blockDim.x + threadIdx.x;
    int idx = row * total_columns + col;
    float out = __ldg(d_in + idx);
    if (out > TOTAL_COL * 64) d_out[idx] = out;
}


__global__ void copy_32B(
    const float* __restrict__ d_in,
    float* __restrict__ d_out,
    size_t total_columns
){
    int row = threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    int idx = row * total_columns + col;
    float out = __ldg(d_in + idx);
    if (out > TOTAL_COL * 64) d_out[idx] = out;
}

int main(void){
    float *h_in = new float[64 * TOTAL_COL];
    float *h_out = new float[64 * TOTAL_COL];

    for (int i = 0; i < 64 * TOTAL_COL; i ++){
        h_in[i] = float(i);
    }

    float *d_in, *d_out;

    cudaMalloc(&d_in, 64 * TOTAL_COL * sizeof(float));
    cudaMalloc(&d_out, 64 * TOTAL_COL * sizeof(float));
    cudaMemcpy(d_in, h_in, 64 * TOTAL_COL * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_out, h_out, 64 * TOTAL_COL * sizeof(float), cudaMemcpyHostToDevice);

    

    // copy_128B<<<grid_dim, block_dim>>>(d_in, d_out, TOTAL_COL);
    // copy_128B<<<grid_dim, block_dim>>>(d_in, d_out, TOTAL_COL);
    // copy_128B<<<grid_dim, block_dim>>>(d_in, d_out, TOTAL_COL);
    // copy_128B<<<grid_dim, block_dim>>>(d_in, d_out, TOTAL_COL);

    cudaProfilerStart();
    dim3 grid_dim(64, TOTAL_COL / 512, 1);
    dim3 block_dim(512, 1, 1);
    copy_128B<<<grid_dim, block_dim>>>(d_in, d_out, TOTAL_COL);
    
    // dim3 grid_dim(TOTAL_COL / 8, 1, 1);
    // dim3 block_dim(8, 64, 1);

    // copy_32B<<<grid_dim, block_dim>>>(d_in, d_out, TOTAL_COL);

    cudaProfilerStop();

    cudaMemcpy(h_out, d_out, 64 * TOTAL_COL * sizeof(float), cudaMemcpyDeviceToHost);

    int errors = 0;
    for (int j=0; j < 64 * TOTAL_COL; j++){
        if (abs(h_out[j] - h_in[j]) > 0.001){
            errors ++;
        }
    }

    if (errors > 0) {
        printf( "COPY does not agree with SEQUENTIAL! %d errors!\n",errors);
    }
    else {
        printf("Results verified: they agree.\n");
    }

    cudaFree(d_in);
    cudaFree(d_out);
    delete h_in;
    delete h_out;
}
