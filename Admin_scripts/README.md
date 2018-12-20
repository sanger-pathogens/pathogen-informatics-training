# Pathogen Informatics Training - Admin scripts

This directory contains a number of scripts that can be used to convert Jupyter Notebooks to PDF. Before merging a notebook into the sanger-pathogens fork, please make sure that you can do a successful conversion of the notebook with the admin scripts.

## Usage
In the notebook directory that you wish to convert, run:

`make_course_pdf.py --no_exec <outprefix> <infile1, infile2, ...>`

Edit the .tex that was generated so that it looks ok. Then run `lualatex` to convert the file to PDF. 

## Dependencies
- lualatex
