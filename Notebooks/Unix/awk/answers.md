# Answers to awk exercises

## Exercise 1
What are the names of the contigs in the file?

    awk -F"\t" '{print $1}' exercises.bed | sort -u


## Exercise 2
How many contigs are there?

    awk -F"\t" '{print $1}' exercises.bed | sort -u | wc -l


## Exercise 3
How many features are on the positive strand?

    awk -F"\t" '$6=="+"' exercises.bed | wc -l


## Exercise 4
How many features are on the negative strand?

    awk -F"\t" '$6=="-"' exercises.bed | wc -l


## Exercise 5
How many genes are there?

    awk -F"\t" '$4 ~ /gene/' exercises.bed | wc -l


## Exercise 6
How many genes have no strand assigned to them (ie the final column is not there)?

    awk -F"\t" '$4 ~ /gene/ && $6 != "-" && $6 != "+"' exercises.bed | wc -l


## Exercise 7
Are any gene names repeated? (Hint: you do not need to find their names, just a yes or no answer. Consider the number of unique gene names.)

First, the number of genes was found earlier:

    awk -F"\t" '$4 ~ /gene/' exercises.bed | wc -l

The number of unique names is:

    awk -F"\t" '$4 ~ /gene/ {print $4}' exercises.bed | sort -u | wc -l

Alternatively, the names can be found like this:

    awk -F"\t" '$4 ~ /gene/ {print $4}' exercises.bed  | sort | uniq -c | awk '$1>1'


## Exercise 9
What is the total score of the repeats?

    awk -F"\t" '$4=="repeat" {score+=$5} END {print score}' exercises.bed


## Exercise 10
How many features are in contig-1?

    awk -F"\t" '$1 == "contig-1"' exercises.bed  | wc -l


## Exercise 11
How many repeats are in contig-1?

    awk -F"\t" '$1 == "contig-1" && $4 == "repeat"' exercises.bed  | wc -l


## Exercise 12
What is the mean score of the repeats in contig-1?

    awk -F"\t" '$1 == "contig-1" && $4 == "repeat" {score+=$5; count++} END{print score/count}' exercises.bed

