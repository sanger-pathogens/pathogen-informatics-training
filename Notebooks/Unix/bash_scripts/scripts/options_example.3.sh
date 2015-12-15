#!/usr/bin/env bash
set -eu

# check that the correct number of options was given.
# If not, then write a message explaining how to use the
# script, and then exit.
if [ $# -ne 2 ]
then
    echo "usage: options_example.3.sh filename number_of_lines"
    echo
    echo "Prints the filename, and the given first number of lines of the file"
    exit
fi

# Use sensibly named variables
filename=$1
number_of_lines=$2

# check if the input file exists
if [ ! -f $filename ]
then
    echo "File '$filename' not found! Cannot continue"
    exit
fi

# If we are still here, then the input file was found
echo filename is: $filename
echo

echo First $number_of_lines lines of file $filename are:
head -n $number_of_lines $filename
