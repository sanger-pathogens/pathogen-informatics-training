FROM jupyter/scipy-notebook

RUN pip install bash_kernel
RUN python -m bash_kernel.install

RUN git clone https://github.com/sanger-pathogens/pathogen-informatics-training.git
WORKDIR $HOME/pathogen-informatics-training/Notebooks