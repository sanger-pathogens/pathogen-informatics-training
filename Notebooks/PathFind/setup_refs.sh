#!/usr/bin/env bash

tutorial_dir=`pwd`
awk -v pwd="$tutorial_dir" -F"\t" 'OFS="\t" {print $1,pwd"/data/refs/"$2 }' data/raw_refs.index > data/refs.index
