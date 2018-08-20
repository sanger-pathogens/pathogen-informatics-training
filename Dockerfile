FROM jupyter/scipy-notebook

# Install bash kernel
RUN pip install bash_kernel
RUN python -m bash_kernel.install

# set user to root to enable installing dependencies
USER root

RUN apt-get update -qq

# Install BLAST
RUN apt-get install -y ncbi-blast+

# Reset original user
USER $NB_UID

# Clone PI-training repo and set workdir
RUN git clone https://github.com/sanger-pathogens/pathogen-informatics-training.git
WORKDIR $HOME/pathogen-informatics-training/Notebooks

