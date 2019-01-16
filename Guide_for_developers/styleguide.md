# Style guide for Pathogen Informatics Training Notebooks
This document contains some guidelines for creating a new Pathogen Informatics Training Notebook. 

* Included in the directory is a template for the index page. When starting on a new notebook, create a directory in pathogen-informatics-training/Notebooks and make a copy of template.ipynb. 
* Put all notebooks in this directory, and not in subdirectories.
* For figures, make a subdirectory called "img" or similar and put all images there.
* Put any data in subdirectories, one for each notebook.
* Rename the copy to index.ipynb and start jupyter notebooks:

`jupyter notebook index.ipynb`

* Below are some general guidelines for the layout of the new notebook:
  - With the exception of scripts, put commands in separate boxes, not together.
  - When using minus signs for equations, make sure to use the real minus sign and not the hyphen.
  - Make sure images are in their own box, and refer to them as:
  
   `![title](path/from/notebookdir)`
  - Give the image a short but decsriptive title, as this will show up in the pdf.
  - At the end of each page, please include a link to the previous page, the next page and the index page. On the index page and the final page, also include a link to the answer sheet.
  - Create one answer sheet for the entire tutorial and divide the answers into the tutorial sections. Add a table of contents at the top of the page (see RNA-Seq tutorial)
  - Please make sure that all commands executed in the tutorial work properly.
  - Also make sure that the notebook can be converted to pdf using the admin scripts as described in pathogen-informatics-training/Admin_scripts/README.md. Include the final pdf and the tex file in the final commit.

* When you are done with the tutorial and it can be converted, please add the conversion command to `.travis.yml`.
* If you add or remove a .ipynb from a tutorial, make sure that you edit `.travis.yml` to reflect this.