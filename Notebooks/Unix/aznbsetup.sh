#!/bin/bash

# As this runs outside of the notebook we need to prepend
# the notebook python to our path

export PATH=/home/nbuser/anaconda3_501/bin:$PATH

# Install bash kernel
pip install bash_kernel
python -m bash_kernel.install
