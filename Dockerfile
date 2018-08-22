FROM jupyter/scipy-notebook

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

# Set up conda channels
RUN conda config --add channels r
RUN conda config --add channels defaults
RUN conda config --add channels conda-forge
RUN conda config --add channels bioconda

# Install SeroBA (also installs dependencies like Ariba, Bowtie2, kmc and Samtools)
RUN conda install -c bioconda seroba

RUN conda install -c conda-forge -c bioconda prokka

# Reset original user
USER $NB_UID

# Clone PI-training repo and set workdir
RUN git clone https://github.com/sanger-pathogens/pathogen-informatics-training.git
WORKDIR $HOME/pathogen-informatics-training/Notebooks

