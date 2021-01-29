import argparse
import sys

import seqlib

parser = argparse.ArgumentParser(
	description='Calculate statistics for genome')
parser.add_argument('--fasta', required = True, type = str,
	metavar = '<path>', help='path to a fasta file, may be compressed')
arg = parser.parse_args()

contig_size = []
nt_count = {}
for name, seq in seqlib.read_fasta(arg.fasta):
    seq = seq.upper()
    contig_size.append(len(seq))
    for base in seq:
        if base not in nt_count:
            nt_count[base] = 1
        elif base in nt_count:
            nt_count[base] += 1

gc_count = nt_count['G'] + nt_count['C']

# Sort contigs longest to shortest
contig_size.sort(reverse = True)

num_contigs = len(contig_size)
shortest_contig = contig_size[-1]
longest_contig = contig_size[0]

total_size = 0
for i in contig_size:
    total_size += i
avg_size = total_size/num_contigs

# Median Calculation
if num_contigs % 2 == 1:
    median_contig = contig_size[int(num_contigs/2)]
elif num_contigs % 2 == 0:
    med1 = contig_size[int(num_contigs/2)]
    med2 = contig_size[int((num_contigs/2) +1)]
    median_contig = (med1 + med2)/2

n50 = 0
val = 0
for size in contig_size:
	val += size
	if val > total_size/2:
		n50 = size
		break

gc_fraction = gc_count/total_size * 100

print(f'Total size: {total_size}')
print(f'Number of contigs: {num_contigs}')
print(f'Shortest contig: {shortest_contig}')
print(f'Longest contig: {longest_contig}')
print(f'Average contig size: {avg_size}')
print(f'Median contig size: {median_contig}')
print(f'N50: {n50}')
print(f'GC Fraction: {gc_fraction}%')
print(f'Letter Counts: {nt_count}')
