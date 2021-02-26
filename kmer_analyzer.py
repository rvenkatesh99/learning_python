import argparse
import seqlib
import itertools
import sys
# command line count + or - strand
# dc palindromes

parser = argparse.ArgumentParser(
	description='Analyze kmers for genome')
parser.add_argument('--fasta', required = True, type = str,
	metavar = '<path>', help='path to a fasta file, may be compressed')
parser.add_argument('--kstart', required = True, type = int,
	metavar = '<int>', help='minimum number of kmers')
parser.add_argument('--klimit', required = True, type = int,
	metavar = '<int>', help='maximum number of kmers')
parser.add_argument('--countn', dest='feature', action='store_true',
    help='Add this flag to count the number of Ns in the genome as part of the kmers')
parser.add_argument('--nocountn', dest='feature', action='store_false',
    help='Default - do not count the number of Ns as part of kmers')
parser.set_defaults(feature=False)

arg = parser.parse_args()

for k in range(arg.kstart, arg.klimit + 1):
    counts = {}
    missing_kmer_list = []

    for name, seq in seqlib.read_fasta(arg.fasta):
        seq = seq.upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i: i+k]
            if arg.feature is True:
                if kmer not in counts:
                    counts[kmer] = 1
                else:
                    counts[kmer] += 1
            else:
                if "N" in kmer:
                    continue
                else:
                    if kmer not in counts:
                        counts[kmer] = 1
                    else:
                        counts[kmer] += 1

    common_kmers = sorted(counts.items(), key=lambda item: item[1],
    		reverse = True)
    if len(counts) < 4**k:
        for tup in itertools.product('ACGT', repeat = k):
            kmer = ''.join(tup)
            if kmer not in counts:
                missing_kmer_list.append(kmer)

    print(f'Kmer size: {k}')
    print(f'Most common kmers: {common_kmers[0:5]}')
    print(f'Least common kmers: {common_kmers[-5:]}')
    print(f'Number of kmers from sequence: {len(common_kmers)}')
    print(f'Number of kmers expected: { 4**k} \n')
    if len(missing_kmer_list) != 0:
        print(f'{4**k - len(common_kmers)} are missing from sequence')
        print(f'Missing kmers: {missing_kmer_list} \n')
