#!/usr/bin/env python3
import random
random.seed(42)

chromosomes = {
    '1': 249250621,
    '2': 243199373,
    '3': 198022430,
    '4': 191154276,
    '5': 180915260,
    '6': 171115067,
    '7': 159138663,
    '8': 146364022,
    '9': 141213431,
    '10': 135534747,
    '11': 135006516,
    '12': 133851895,
    '13': 115169878,
    '14': 107349540,
    '15': 102531392,
    '16': 90354753,
    '17': 81195210,
    '18': 78077248,
    '19': 59128983,
    '20': 63025520,
    '21': 48129895,
    '22': 51304566,
    'X': 155270560,
    'Y': 59373566,
    'MT': 16569,
    'GL000226.1': 15008,
    'GL000229.1': 19913,
    'GL000231.1': 27386,
    'GL000210.1': 27682,
    'GL000239.1': 33824,
    'GL000235.1': 34474,
}


ordered_chromosomes = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    'X',
    'Y',
    'MT',
    'GL000226.1',
    'GL000229.1',
    'GL000231.1',
    'GL000210.1',
    'GL000239.1',
    'GL000235.1',
]



total_genes = 1


def make_repeat(ref_name, ref_length, start, min_length=100, max_length=5000, invert_chance=2, no_score_chance=2):
    repeat_types = ['ALU', 'LINE', 'SINE']
    length = random.randint(min_length, max_length)
    end = start + length - 1
    source = 'source' + str(random.randint(11,15))

    if no_score_chance >= random.randint(0, 100):
        score = random.choice(['.', '-1'])
    else:
        score = random.randint(0, 100)

    line = '\t'.join([
        ref_name, 
        source,
        'repeat',
        str(start),
        str(end),
        str(score),
        '.',
        '.'
    ])

    return line, end


def make_gene(ref_name, ref_length, start, min_length=100, max_length=999, invert_chance=2, frameshift_chance=2, no_strand_chance=1, no_name_chance=1):
    global total_genes
    assert start + min_length < ref_length
    length = 3 * random.randint(int(min_length/3), int((max_length - 1)/3))
    end = min(start + length - 1, ref_length)
    source = 'source' + str(random.randint(1,10))

    if invert_chance >= random.randint(0, 100) and source in ['source1', 'source2', 'source3', 'source8']:
        start, end = end, start

    if frameshift_chance >= random.randint(0, 100) and source in ['source3', 'source4', 'source5']:
        end += random.randint(1, 2)

    if no_strand_chance >= random.randint(0, 100) and source in ['source1', 'source6', 'source7']:
        strand = '.'
    else:
        strand = random.choice(['-', '+'])

    line = '\t'.join([
        ref_name, 
        source,
        'gene',
        str(start),
        str(end),
        str(round(100 * random.random(), 1)),
        strand,
        str(random.randint(0,2))
    ])

    if no_name_chance < random.randint(0, 100):
        line += '\tname=gene' + str(total_genes)
        if 0.03 > random.random():
            total_genes += 1
        
    return line, max(start, end)


def update_pos(pos, ref_length):
    if ref_length <= 100000:
        return pos + random.randint(1000, 5000)
    else:
        return pos + random.randint(10000, 100000)
    
     

lines_of_file = 10000
total_bases = sum(chromosomes.values())


max_gene_length = 999
max_repeat_length = 5000
max_feature_length = max(max_gene_length, max_repeat_length)


for ref in ordered_chromosomes:
    ref_length = chromosomes[ref]
    pos = random.randint(0, 1000)

    while pos + max_feature_length < ref_length:
        if 10 > random.randint(0, 100) and pos:
            new_line, end = make_repeat(ref, ref_length, pos, max_length=max_repeat_length)
        else:
            new_line, end = make_gene(ref, ref_length, pos, max_length=max_gene_length)

        pos = update_pos(end, ref_length)
        print(new_line)

