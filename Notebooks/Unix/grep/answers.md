# Answers to grep exercises

## Exercise 1
Make a grep command that outputs just the lines with the sequence names.

    grep "^>" exercises.fasta


## Exercise 2
How many sequences are in the file?

We can use -c to count the number of matches

    grep -c "^>" exercises.fasta

Or pipe into wc

    grep "^>" exercises.fasta | wc -l


## Exercise 3
Do any sequence names have spaces in them? What are their names?

One option is two greps piped together:
    
    grep "^>" exercises.fasta | grep " "

Alternatively, in one regular expression

    grep "^>.* .*" exercises.fasta



## Exercise 4
Make a grep command that outputs just the lines with the sequences, not the names.

    grep -v "^>" exercises.fasta



## Exercise 5
How many sequences contain unknown bases (an "n" or "N")?

    grep -v "^>" exercises.fasta | grep -c -i n



## Exercise 6
Are there any sequences that contain non-nucleotides (something other than A, C, G, T or N)?

    grep -v "^>" exercises.fasta | grep -i -v "^[acgtn].*$"

Alternatively, we can use the ^ to ask for matches NOT in the alphabet [acgtn]

     grep -v "^>" exercises.fasta | grep -i "[^ACGTN]"



## Exercise 7
How many sequences contain the 5' cut site GCWGC (where W can be an A or T) for the restriction enzyme AceI?

    grep -v "^>" exercises.fasta | grep -c "GC[AT]GC"



## Exercise 8 
Are there any sequences that have the same name? You do not need to find the actual repeated names, just whether any names are repeated. (Hint: it may be easier to first discover how many unique names there are).

We found the total number of sequences earlier:
    
    grep -c "^>" exercises.fasta

... which outputs 1000

This finds the number of unique names:

    grep "^>" exercises.fasta | sort | uniq | wc -l

... which outputs 999.

Therefore there is 1000 - 999 = 1 name repeated.
