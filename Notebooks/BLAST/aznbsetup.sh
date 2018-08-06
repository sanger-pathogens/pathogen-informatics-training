#!/bin/bash

start=`date +%s`

###########################################
#                 MANUAL                  #
###########################################

# As this runs outside of the notebook we need to prepend the notebook conda to our path
export PATH=/home/nbuser/anaconda3_501/bin:$PATH

# Install bash kernel
pip install bash_kernel
python -m bash_kernel.install

# Make bin directory for programs
mkdir bin && cd bin

# Download blast+
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.7.1+-x64-linux.tar.gz
tar -xf ncbi-blast-2.7.1+-x64-linux.tar.gz
rm ncbi-blast-2.7.1+-x64-linux.tar.gz

# Symlink executables to bin directory in PATH
# export PATH doesn't seem to persist into notebook
ln -s /home/nbuser/bin/ncbi-blast-2.7.1+/bin/* /home/nbuser/.local/bin

###########################################
#                 CONDA                   #
###########################################

# As this runs outside of the notebook we need to prepend the notebook conda to our path source
#source /home/nbuser/anaconda3_501/bin/activate

# Install bash kernel
#pip install bash_kernel
#python -m bash_kernel.install

# Set up proxy 
#http_proxy=http://webproxy:3128
#https_proxy=http://webproxy:3128
#export http_proxy
#export https_proxy

# Install blast+
#conda config --add channels bioconda
#conda install -c bioconda blast -y

end=`date +%s`
runtime=$((end-start))
echo "Script took "$runtime" seconds"
