#### Using Docker

Get the source code
```shell
git clone https://github.com/apuaaChen/vectorSparse.git && cd vectorSparse
```

We provides a Dockerfile that builds the proper environment with all dependencies. Note that nvidia-docker must be installed to run on GPU. To build the image, run the following command:
```shell
docker build -t vectorsparse .
```
To launch the container
```shell
docker run -it --gpus all --name <your_container_name> -d -v <host_dataset_dir>:/raid/dataset -v <host_dir>/vectorSparse:/projects/vectorSparse vectorsparse
```
Then, compile the source code with
```shell
bash setup.sh
```
To obtain the results in Figure 17, run
```shell
python3 launch.py --exp spmm
```
The result will be shown in spmm_speedup_rn50_combo.pdf

To obtain the results in Figure 18, run
```shell
python3 launch.py --exp sddmm
```
The result will be shown in sddmm_speedup_rn50_combo.pdf