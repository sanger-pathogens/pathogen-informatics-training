#!/bin/bash

infile=data/sequence.txt.$LSB_JOBINDEX
echo "Reading $infile"

input=$(<$infile)
echo "Input sequence: $input"

output=$(echo $input | tr 'ATGC' 'TACG')
echo "Complementary sequence: $output"

echo "Done"
