#!/usr/bin/env python3

import argparse
import file_utils


parser = argparse.ArgumentParser(
    description = 'Converts ipynb to latex file. Does a few fixes with formatting not done by jupyter',
    usage = '%(prog)s [options] <infile> <outfile>')
parser.add_argument('infile', help='Name of input ipynb')
parser.add_argument('outfile', help='Name of output tex file')
options = parser.parse_args()

converter = file_utils.Ipynb_to_tex_converter(options.infile, options.outfile)
converter.run()
