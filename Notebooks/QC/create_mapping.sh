#!/bin/sh

# Create the reference genome index, necessary for bwa alignment
bwa index data/Saccharomyces_cerevisiae.EF4.68.dna.toplevel.fa


# Several commands are piped one into another:
#   - align the lane fastq files with bwa
#   - convert the sam output to bam
#   - sort the bams
#   - index the bams
#
bwa mem -M \
    -R '@RG\tID:lane1\tSM:60A_Sc_DBVPG6044' \
    data/Saccharomyces_cerevisiae.EF4.68.dna.toplevel.fa \
    data/lane1/s_7_1.fastq \
    data/lane1/s_7_2.fastq |
samtools view -b - |
samtools sort -T tmp.lane1 -o data/lane1.sorted.bam
samtools index data/lane1.sorted.bam