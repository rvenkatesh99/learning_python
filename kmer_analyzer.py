import seqlib
import itertools
import sys
# command line count + or - strand
# command ine upper lower case
# count ns or not
# dc palindromes
for k in range(2, 50):
    counts = {}

    for name, seq in seqlib.read_fasta("mini.fa"):
        print(name)
        seq = seq.upper()
        for i in range(len(seq) - k + 1):
            kmer = seq[i: i+k]
            if "N" in kmer:
                continue
            if kmer not in counts:
                counts[kmer] = 1
            else:
                counts[kmer] += 1

    common_kmers = sorted(counts.items(), key=lambda item: item[1],
    		reverse = True)
    print(common_kmers[0:5])
    print(common_kmers[-5:])
    print(len(common_kmers), 4**k)
    # if len(counts) < 4**k:
    #     for tup in itertools.product('ACGT', repeat = k):
    #         kmer = ''.join(tup)
    #         if kmer not in counts:
    #             print(kmer)
