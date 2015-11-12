#!/usr/bin/env bash
filename=$1
number_of_lines=$2

echo filename is: $filename
echo

echo First $number_of_lines lines of file $filename are:
head -n $number_of_lines $filename
