#!/usr/bin/env python3

import subprocess
import os
import argparse
import file_utils


parser = argparse.ArgumentParser(
    description = 'Cats tex files. Uses header from first file listed.',
    usage = '%(prog)s [options] <outprefix> <infile1, infile2, ...>')
parser.add_argument('outprefix', help='Prefix of output files')
parser.add_argument('infiles', nargs='+', help='Name of input ipynb files')
options = parser.parse_args()


tex_files = []

for filename in options.infiles:
    outfile = options.outprefix + '.' + str(len(tex_files)) + '.tex'
    tex_files.append(outfile)
    print('Converting', filename, 'to temporary tex file', outfile)
    converter = file_utils.Ipynb_to_tex_converter(filename, outfile)
    converter.run()

assert len(tex_files) == len(options.infiles)


final_tex_file = options.outprefix + '.tex'
print(len(tex_files), 'files converted. Combining into to one tex file', final_tex_file)
catter = file_utils.Tex_catter(tex_files, final_tex_file)
catter.run()

final_pdf = options.outprefix + '.pdf'
print('Making final pdf', final_pdf)


try:
    subprocess.check_output('pdflatex ' + final_tex_file, shell=True, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as error:
    sys.exit('Error running latex')

to_delete = [options.outprefix + '.' + x for x in ['aux', 'log', 'out']]
to_delete.extend(tex_files)


print('Cleaning files:', *to_delete)

for filename in to_delete:
    os.unlink(filename)

