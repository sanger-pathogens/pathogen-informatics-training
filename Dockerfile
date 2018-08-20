FROM jupyter/scipy-notebook

# Install bash kernel
RUN pip install bash_kernel
RUN python -m bash_kernel.install

# set user to root to enable installing dependencies
USER root

RUN apt-get update -qq

# Install dependencies for BLAST tutorial
RUN apt-get install -y ncbi-blast+

# Install dependencies for ARIBA tutorial
RUN apt-get install --no-install-recommends -y \
  build-essential \
  cd-hit \
  curl \
  git \
  libbz2-dev \
  liblzma-dev \
  mummer \
  unzip \
  wget \
  zlib1g-dev

USER $NB_UID

RUN pip install ariba
RUN wget -q http://downloads.sourceforge.net/project/bowtie-bio/bowtie2/2.2.9/bowtie2-2.2.9-linux-x86_64.zip \
  && unzip bowtie2-2.2.9-linux-x86_64.zip \
  && rm bowtie2-2.2.9-linux-x86_64.zip
# Need MPLBACKEND="agg" to make matplotlib work without X11, otherwise get the error
# _tkinter.TclError: no display name and no $DISPLAY environment variable
ENV ARIBA_BOWTIE2=/home/jovyan/bowtie2-2.2.9/bowtie2 ARIBA_CDHIT=cdhit-est MPLBACKEND="agg"

USER root

# Reset original user
USER $NB_UID

# Clone PI-training repo and set workdir
RUN git clone https://github.com/sanger-pathogens/pathogen-informatics-training.git
WORKDIR $HOME/pathogen-informatics-training/Notebooks

