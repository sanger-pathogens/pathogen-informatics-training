#!/usr/bin/env python3

import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=argparse.FileType('r'))
parser.add_argument('-i', action='store_true')

args = parser.parse_args()

original_notebook = json.loads(args.input_file.read())
args.input_file.close()

if args.i:
  output_file = open(args.input_file.name, 'w')
else:
  output_file = sys.stdout

notebook_without_output = dict(original_notebook)
notebook_without_output['cells'] = []

for cell in original_notebook['cells']:
  if cell.get('execution_count'):
    cell['execution_count'] = None
  if cell.get('outputs'):
    cell['outputs'] = []
  notebook_without_output['cells'].append(cell)
 
json.dump(notebook_without_output, 
          output_file,
          sort_keys=True,
          indent=1,
          separators=(",",": "),
          ensure_ascii=True)
