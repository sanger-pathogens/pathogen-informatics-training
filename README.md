# Pathogen Informatics Training
A set of bioinformatics training courses developed by Pathogen Informatics at Wellcome Sanger Institute.

[![Build Status](https://travis-ci.org/sanger-pathogens/pathogen-informatics-training.svg?branch=master)](https://travis-ci.org/sanger-pathogens/pathogen-informatics-training)   
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-brightgreen.svg)](https://github.com/sanger-pathogens/pathogen-informatics-training/blob/master/LICENSE)

## Content
  * [Introduction](#introduction)
  * [Installation](#installation)
    * [Docker](#docker) 
  * [Usage](#usage)
  * [License](#license)
  * [Feedback/Issues](#feedbackissues)

## Introduction
These bioinformatics training courses use Jupyter notebooks to provide pathogen informatics training and the following notebooks are avaiable:

 * UNIX for Bioinformatics
 * Introduction to BLAST
 * NGS Data Formats and QC
 * An Introduction to IGV
 * RNA-Seq Expression Analysis 
 * Differential Expression and GO Term Analysis using DEAGO
 * Pangenome Construction using Roary
 * Antimicrobial Resistance Identification using ARIBA
 * Serotype Detection using SeroBA
 * PathFind (pf) scripts
 * ChiP-Seq
 * LSF

## Installation
The courses use [Jupyter](http://jupyter.org/) notebooks, which means that Jupyter must be installed to use them. Please see the [Jupyter installation instructions](http://jupyter.readthedocs.org/en/latest/install.html) for details.
  
If you are running Jupyter on MacOS you may have to install the bash kernel. To do so, run the following commands:
  
    pip install bash_kernel
   
    python -m bash_kernel.install
  
The courses assume that you have the relevant tools installed (e.g. [ARIBA](https://github.com/sanger-pathogens/ariba) and [SeroBA](https://github.com/sanger-pathogens/seroba)). Further information about the relevant dependencies can be found inside each individual notebook.

### Docker
The following tutorials can be run in a Docker container:

 * UNIX for Bioinformatics
 * Introduction to BLAST
 * Antimicrobial Resistance Identification using ARIBA
 * Serotype Detection using SeroBA

First install Docker, then pull down the Docker image:

    docker pull sangerpathogens/pathogen-informatics-training

To start the Notebook, run:

    docker run -p 8888:8888 -d sangerpathogens/pathogen-informatics-training jupyter notebook

This will print a URL with a token. Copy and paste this in your browser. This will open the notebook in the "Notebooks" directroy. Click on the index.ipynb and navigate your way to the desired notebook from there.

If for some reason you need to close the tutorial and want to continue at a later date (provided that you have saved your progress in the notebooks using the save button), you can restart the container by running:

    docker start -a CONTAINER_ID

Where CONTAINER_ID is the id of the container. You can find out what the id of the container is by running:

    docker container ls -a

Again, copy the URL into your browser and you are ready to pick up where you left off.

## Usage
Clone this repository:

    git clone https://github.com/sanger-pathogens/pathogen-informatics-training.git

Start Jupyter at the main index page to view the available courses:

    jupyter notebook pathogen-informatics-training/Notebooks/index.ipynb

Select a course and follow the instructions given in the notebook.

## License
This is free software, licensed under [GPLv3](https://github.com/sanger-pathogens/pathogen-informatics-training/blob/master/LICENSE).

## Feedback/Issues
Please report any issues to the [issues page](https://github.com/sanger-pathogens/pathogen-informatics-training/issues) or email path-help@sanger.ac.uk
