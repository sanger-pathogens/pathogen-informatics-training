# Pathogen Informatics Training - Admin scripts

This directory contains a number of scripts that can be used to convert Jupyter Notebooks to PDF. Before merging a notebook into the sanger-pathogens fork, please make sure that it conforms to the style guide in `Guide_for_developers` and that you can do a successful conversion of the notebook with the admin scripts.

## Usage
Make sure that your version of MacTeX (in particular lualatex) is up to date.  

In the notebook directory that you wish to convert, run:

`../../make_course_pdf.py --no_exec <outprefix> <infile1, infile2, ...>`

Edit the .tex that was generated so that it looks ok (for instance by adding page breaks, checking that text wrapping in command blocks don't exceed page width, and fixing image positions). Then run `lualatex` to convert the file to PDF. 

## Dependencies
- [MacTeX](https://tug.org/mactex/), texlive or similar
- pandoc
- anything listed in .travis.yml

## Hints
* If an image wraps over a new page, it can cause blank spaces and unusual formatting. To get around it, put a /newpage line in the .tex file before the image.
* If you get errors about \faKeyboardO, make sure your version of mactex/texlive is up to date (for travis, this meant running tests in xenial). 