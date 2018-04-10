# Pathogen Informatics Training
A set of courses for pathogen informatics training.

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-brightgreen.svg)](https://github.com/sanger-pathogens/pathogen-informatics-training/blob/master/LICENSE)

## Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Usage](#usage)
  * [License](#license)
  * [Feedback/Issues](#feedbackissues)

## Introduction
The pathogen informatics training courses use Jupyter notebooks to provide pathogen informatics training. There are currently 5 independent notebooks:

 * UNIX
 * ARIBA
 * SeroBA
 * BLAST
 * DEAGO

## Installation
The courses use [Jupyter](http://jupyter.org/) notebooks, which means that Jupyter must be installed to use them. Please see the [Jupyter installation instructions](http://jupyter.readthedocs.org/en/latest/install.html) for details.
  
If you are running Jupyter on MacOS you may have to install the bash kernel. To do so, run the following commands:
  
    pip install bash_kernel
   
    python -m bash_kernel.install
  
Most of the courses assume that you have the relevant tools installed (e.g. [ARIBA](https://github.com/sanger-pathogens/ariba) and [SeroBA](https://github.com/sanger-pathogens/seroba)). Further information about the relevant dependencies can be found inside each indsvidual notebook.

## Usage
Clone this repository:

    git clone https://github.com/sanger-pathogens/pathogen-informatics-training.git

Start Jupyter at the main index page to view the available courses:

    jupyter notebook pathogen-informatics-training/Notebooks/index.ipynb

Select a course and follow the instructions give in the notebook.

## License
This is free software, licensed under [GPLv3](https://github.com/sanger-pathogens/pathogen-informatics-training/blob/master/LICENSE).

## Feedback/Issues
Please report any issues to the [issues page](https://github.com/sanger-pathogens/pathogen-informatics-training/issues) or email path-help@sanger.ac.uk
