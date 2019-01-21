#!/bin/bash

input=$(<data/sequence.txt)
echo "Input sequence: $input"

output=$(echo $input | tr 'ATGC' 'TACG')
echo "Complementary sequence: $output"
