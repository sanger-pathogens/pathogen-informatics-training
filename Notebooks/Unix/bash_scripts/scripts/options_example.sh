#!/usr/bin/env bash

echo filename is: $1
echo

echo First $2 lines of file $1 are:
head -n $2 $1
