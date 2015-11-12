#!/usr/bin/env python3

import argparse
import file_utils


parser = argparse.ArgumentParser(
    description = 'Cats tex files. Uses header from first file listed.',
    usage = '%(prog)s [options] <outfile> <infile1, infile2, ...>')
parser.add_argument('outfile', help='Name of output tex file')
parser.add_argument('infiles', nargs='+', help='Name of input tex files')
options = parser.parse_args()


catter = file_utils.Tex_catter(options.infiles, options.outfile)
catter.run()

