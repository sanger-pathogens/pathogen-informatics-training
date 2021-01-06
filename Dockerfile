FROM jupyter/scipy-notebook:58169ec3cfd3
# jupyter/scipy-notebook:87210526f381 2019-01-09 was used to build pathogen-informatics-training image from github tag NGS_feb_2019
# jupyter/scipy-notebook:58169ec3cfd3 2019-08-04 tested for RT666607 on 2019-08-06

ENV   INSTALL_DIR=$HOME/pathogen-informatics-training

# assert inheritance of NB_UID from base image
RUN   bash -c "if [[ \"\" == \"$NB_UID\" ]]; then echo \"user ID variable NB_UID has not been set\" && exit 255; fi"

# Install bash kernel
RUN   pip install bash_kernel
RUN   python -m bash_kernel.install

# set user to root to enable installing dependencies
USER  root

RUN   apt-get  update -qq && \
      apt-get  install -y apt-utils

# Install dependencies for BLAST tutorial
RUN   apt-get  install -y ncbi-blast+

# Install dependencies for ARIBA and SeroBA tutorials
RUN   apt-get  install --no-install-recommends -y \
               build-essential \
               git \
               libbz2-dev \
               liblzma-dev \
               unzip \
               wget \
               zlib1g-dev\
               subversion

# install SeroBA
# https://github.com/sanger-pathogens/seroba#debian-testing-ubuntu-1710 suggests apt install of ariba
# bowtie2 cd-hit and mummer also known to be required
# libcurl4-gnutls-dev libssl-dev provide curl.h and openssl/hmac.h (respectively), prevent errors in pip install
RUN   apt-get  install --yes ariba bowtie2 cd-hit curl libcurl4-gnutls-dev libssl-dev mummer
RUN   mkdir kmc && \
      cd kmc && \
      wget -O- https://github.com/refresh-bio/KMC/releases/download/v3.0.0/KMC3.linux.tar.gz | tar xzvf - && \
      export PATH=$PWD:$PATH
# most recent pymummer (0.11.0 on 20190806) incompatible with ariba
# also note pip cache is owned by uid $NB_UID
RUN   PIP=`which pip` && sudo -u "#$NB_UID" $PIP install pymummer==0.10.3 seroba

# conda set up
RUN   conda update -n base conda && \
      conda config --add channels r && \
      conda config --add channels defaults && \
      conda config --add channels conda-forge && \
      conda config --add channels bioconda

# # SeroaBA build from github source (above), rather than conda
# # # Install SeroBA (also installs dependencies like Ariba, Bowtie2, kmc and Samtools)
# # RUN conda install -c bioconda seroba

RUN conda install -c conda-forge -c bioconda prokka

# Reset original user (as used in jupyter/minimal-notebook Dockerfile)
USER  $NB_UID

# Clone PI-training repo and set workdir
###RUN git clone https://github.com/sanger-pathogens/pathogen-informatics-training.git
RUN      mkdir -p $INSTALL_DIR
# using NB_UID variable with the chown argument works for my local docker build, but not in DockerHub
# COPY     --chown=$NB_UID . $INSTALL_DIR/
COPY     . $INSTALL_DIR/
USER     root
RUN      chown -R $NB_UID $INSTALL_DIR
USER     $NB_UID
# RUN      find $INSTALL_DIR/ -maxdepth 1 -ls

WORKDIR  $INSTALL_DIR/Notebooks

# RUN which python && python --version && which pip && pip --version

