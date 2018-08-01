#!/usr/bin/env bash

for r1 in SBP*_1.fastq
do
  echo $r1
  sample=${r1/_1.fastq/}
  echo "Processing sample: "$sample
  hisat2 --max-intronlen 10000 -x PccAS_v3_hisat2.idx -1 $sample'_1.fastq' -2 $sample'_2.fastq' \
  | samtools view -b - \
  | samtools sort -o $sample"_sorted.bam" - \
  && samtools index $sample"_sorted.bam" 
done
