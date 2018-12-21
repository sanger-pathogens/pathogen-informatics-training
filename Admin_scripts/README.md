# Pathogen Informatics Training - Admin scripts

This directory contains a number of scripts that can be used to convert Jupyter Notebooks to PDF. Before merging a notebook into the sanger-pathogens fork, please make sure that it conforms to the styleguide in `Guide_for_developers` and that you can do a successful conversion of the notebook with the admin scripts.

## Usage
Make sure that your version of MacTeX (in particular lualatex) is up to date.  

In the notebook directory that you wish to convert, run:

`../../make_course_pdf.py --no_exec <outprefix> <infile1, infile2, ...>`

Edit the .tex that was generated so that it looks ok. Then run `lualatex` to convert the file to PDF. 

## Dependencies
- [MacTeX](https://tug.org/mactex/) or similar