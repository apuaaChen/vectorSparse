FROM nvidia/cuda:11.2.2-devel-ubuntu18.04

MAINTAINER zdchen <chenzd15thu@ucsb.edu>

RUN mkdir projects && cd projects

# Install Git
RUN apt-get update && apt-get install git

# Install Sputnik Dependencies
RUN apt-get -y update --fix-missing
RUN apt-get install -y emacs wget libgoogle-glog-dev
RUN apt-get install -y software-properties-common
RUN apt-get update
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null
RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main'
RUN apt-get update && apt-get install -y cmake

# Build sputnik
RUN git clone https://github.com/google-research/sputnik.git
RUN cd ./sputnik
RUN mkdir build && cd build
RUN cmake .. -DCMAKE_BUILD_TYPE=Release -DCUDA_ARCHS="70"
RUN make -j12

ENV CUDA_INSTALL_PATH=/usr/local/cuda-11.2
ENV PATH=$CUDA_INSTALL_PATH/bin:$PATH
ENV LD_LIBRARY_PATH=projects/sputnik/build/sputnik/

# install Python3.8
RUN apt-get install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install python3.8

# install pip3
RUN apt-get update
RUN apt-get -y install python3-pip

# install python libraries
RUN pip3 install numpy
RUN pip3 install matplotlib

# install nsight compute
RUN apt-get install nsight-compute