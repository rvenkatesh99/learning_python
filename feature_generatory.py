import random
import sys
chr = ['chr1', 'chr2', 'chr3', 'chr4']
clen = 10000000
min = 50
max = 5000

n = int(sys.argv[1])
for i in range(n):
    c = random.choice(chr)
    beg_coord = random.randint(1, clen)
    end_coord = beg_coord + random.randint(min, max)
    print(f'{c}\t{beg_coord}\t{end_coord}')
