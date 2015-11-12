#!/usr/bin/env python3
import random
random.seed(42)


def make_repeat(ref_name, ref_length, start, min_length=100, max_length=5000):
    repeat_types = ['ALU', 'LINE', 'SINE']
    length = random.randint(min_length, max_length)
    end = start + length - 1

    line = '\t'.join([
        ref_name, 
        str(start),
        str(end),
        'repeat',
        str(random.randint(0, 1000)),
    ])

    return line, end


def make_gene(ref_name, ref_length, start, min_length=100, max_length=999, invert_chance=2, no_strand_chance=1):
    global total_genes
    assert start + min_length < ref_length
    length = 3 * random.randint(int(min_length/3), int((max_length - 1)/3))
    end = min(start + length - 1, ref_length)
    source = 'source' + str(random.randint(1,10))

    if invert_chance >= random.randint(0, 100) and source in ['source1', 'source2', 'source3', 'source8']:
        start, end = end, start

    gene = 'gene-' + str(total_genes)
    if 0.03 < random.random():
        total_genes += 1


    line = '\t'.join([
        ref_name, 
        str(start),
        str(end),
        gene,
        str(round(100 * random.random(), 1)),
    ])

    if no_strand_chance < random.randint(0, 100):
        line += '\t' + random.choice(['-', '+'])
    
    return line, max(start, end)


def update_pos(pos, ref_length):
    if ref_length <= 100000:
        return pos + random.randint(1000, 5000)
    else:
        return pos + random.randint(10000, 100000)
    



total_contigs = 5
contig_names = ['contig-' + str(x+1) for x in range(total_contigs)]
contig_lengths = {name: random.randint(3000000, 5000000) for name in contig_names}

max_gene_length = 999
max_repeat_length = 5000
max_feature_length = max(max_gene_length, max_repeat_length)
total_genes = 1


for contig in contig_names:
    contig_length = contig_lengths[contig]
    pos = random.randint(0, 1000)

    while pos + max_feature_length < contig_length:
        if 10 > random.randint(0, 100) and pos:
            new_line, end = make_repeat(contig, contig_length, pos, max_length=max_repeat_length)
        else:
            new_line, end = make_gene(contig, contig_length, pos, max_length=max_gene_length)

        pos = update_pos(end, contig_length)
        print(new_line)

