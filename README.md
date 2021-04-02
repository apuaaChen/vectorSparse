#### Using Docker

Step 1: Get the source code
```shell
git clone https://github.com/apuaaChen/vectorSparse.git && cd vectorSparse
```

Step 2: We provides a Dockerfile that builds the proper environment with all dependencies. Note that nvidia-docker must be installed to run on GPU. To build the image, run the following command:
```shell
docker build -t vectorsparse .
```

Step 3: Get The dataset
We use the [Deep Learning Matrix Collection](https://storage.googleapis.com/sgk-sc2020/dlmc.tar.gz). Please download the dataset and put it into the directory <host_dataset_dir>. The directory will be something like  <host_dataset_dir>/dlmc/rn50/....

Step 4: To launch the container
```shell
docker run -it --gpus all --name <your_container_name> -v <host_dataset_dir>:/raid/datasets -v <host_dir>/vectorSparse:/projects/vectorSparse vectorsparse
```
So that in the container, the sparse matrices will be available at /raid/datasets/dlmc/rn50/...

Step 5: Compile the source code with
```shell
cd vectorSparse
bash setup.sh
```

Step 6.1: To obtain the results in Figure 17, run
```shell
python3 launch.py --exp spmm
```
The result will be shown in spmm_speedup_rn50_combo.pdf

Step 6.2: To obtain the results in Figure 18, run
```shell
python3 launch.py --exp sddmm
```
The result will be shown in sddmm_speedup_rn50_combo.pdf

***

The DLMC dataset and sputnik library are from this paper
```
@inproceedings{sgk_sc2020,
  author    = {Trevor Gale and Matei Zaharia and Cliff Young and Erich Elsen},
  title     = {Sparse {GPU} Kernels for Deep Learning},
  booktitle = {Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, {SC} 2020},
  year      = {2020},
}
```