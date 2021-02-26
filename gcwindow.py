import seqlib
import sys

def gc(seq):
    g = seq.count('G')
    c = seq.count('C')
    a = seq.count('A')
    t = seq.count('T')
    if (a + g +c +t) == 0:
        return None
    return((g+c)/(a+c+t+g)) # GC percentage
    return((g-c)/(g+c)) # GC skew

window = int(sys.argv[2])
step = int(sys.argv[3])
for name, chrom in seqlib.read_fasta(sys.argv[1]):
    chrom = chrom.upper()
    f = name.split()
    # give range operator start, end, and step size
    for i in range(0, len(chrom) - window + 1, step):
        seq = chrom[i:i+window]
        print(f[0], i+1, i + window, gc(seq))
