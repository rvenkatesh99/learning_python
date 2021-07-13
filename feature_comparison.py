import sys
# sort with a binary search (boundaries) - lookup table

def read_features(file):
    features = {}
    with open(file) as fp:
        for line in fp.readlines():
            (chr, beg, end) = line.split()
            if chr not in features:
                features[chr] = []
                features[chr].append((int(beg), int(end)))
        return features

def overlap(f1, f2):
    c1, b1, e1 = f1
    c2, b2, e2, = f2
    if c1 != c2: return False

    if b1 >= b2 and b1 <= e2: return True
    elif e1 >= b2 and e1 <= e2: return True
    elif b1 <= b2 and e1 >= e2: return True
    else: return False

def overlap2(f1, f2):
    b1, e1 = f1
    b2, e2 = f2

    if b1 >= b2 and b1 <= e2: return True
    elif e1 >= b2 and e1 <= e2: return True
    elif b1 <= b2 and e1 >= e2: return True
    else: return False

features1 = read_features(sys.argv[1])
features2 = read_features(sys.argv[2])

overlap_list = []
for chr in features1:
    for f1 in features1:
        for f2 in features2:
            if overlap2(f1, f2):
                overlap_list.append((f1, f2))

"""
overlap_list = []
for f1 in features1:
    for f2 in features2:
        if overlap(f1, f2):
            overlap_list.append((f1, f2))
"""

for ol in overlap_list:
    print(ol)

"""
    genes: 20k
    exons: 100k
    SNPs: 610k

"""
