FROM jupyter/scipy-notebook:87210526f381
# jupyter/scipy-notebook:87210526f381 2019-01-09 was used to build pathogen-informatics-training image from github tag NGS_feb_2019

RUN which python && python --version && which pip && pip --version

# Install bash kernel
RUN pip install bash_kernel
RUN python -m bash_kernel.install

# set user to root to enable installing dependencies
USER root

RUN apt-get update -qq

# Install dependencies for BLAST tutorial
RUN apt-get install -y ncbi-blast+

# Install dependencies for ARIBA and SeroBA tutorials
RUN apt-get install --no-install-recommends -y \
  build-essential \
  git \
  libbz2-dev \
  liblzma-dev \
  unzip \
  wget \
  zlib1g-dev\
  subversion

RUN conda update -n base conda

# Set up conda channels
RUN conda config --add channels r
RUN conda config --add channels defaults
RUN conda config --add channels conda-forge
RUN conda config --add channels bioconda

# Install SeroBA (also installs dependencies like Ariba, Bowtie2, kmc and Samtools)
RUN conda install -c bioconda seroba

RUN conda install -c conda-forge -c bioconda prokka

# Reset original user (as used in jupyter/minimal-notebook Dockerfile)
RUN   bash -c "if [[ \"\" == \"$NB_UID\" ]]; then echo \"user ID variable NB_UID has not been set\" && exit 255; fi"
USER  $NB_UID

# Clone PI-training repo and set workdir
###RUN git clone https://github.com/sanger-pathogens/pathogen-informatics-training.git
RUN      mkdir -p $HOME/pathogen-informatics-training
COPY     --chown=$NB_UID . $HOME/pathogen-informatics-training/

WORKDIR  $HOME/pathogen-informatics-training/Notebooks

RUN which python && python --version && which pip && pip --version

