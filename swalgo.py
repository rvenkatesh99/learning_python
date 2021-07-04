s1 = "mmlk"
s2 = 'mmilk'
max = 0
max_i = None
max_j = None

match = 1
mismatch = -1
gap = -1

def display(m):
    for row in m:
        print(row)
# 2 matrices - scores + traceback
# memory allocation
score = []
trace = []

for i in range(len(s1) + 1):
    s = []
    t = []
    for j in range(len(s2) +1):
        s.append(None)
        t.append(None)
    score.append(s)
    trace.append(t)
# Initialization
for i in range(len(s1) + 1): # first column
    score[i][0] = 0
    trace[i][0] = 'N'
for i in range(len(s2) + 1): # first row
    score[0][i] = 0
    trace[0][i] = 'N'

# fill
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        display(score)
        print(i, j-1)
        up = score[i][j - 1] + gap
        left = score[i-1][j] + gap
        if s1[i-1] == s2[j-1]:
            diag = score[i-1][j-1] + match
        else:
            diag = score[i-1][j-1] + mismatch
        if diag > up and  diag > left and diag > 0:
            score[i][j] = diag
            trace[i][j] = 'd'
            if score[i][j] > max:
                max = score[i][j]
                max_i = i
                max_j = j
        elif up > left and up > 0:
            score[i][j] = up
            trace[i][j] = 'u'
        elif left > 0:
            score[i][j] = left
            trace[i][j] = 'l'
        else:
            score[i][j] = 0
            trace[i][j] = ' '

display(score)
display(trace)
seq1_align = []
seq2_align = []

# Traceback
while score[max_i][max_j] > 0:
    print(max_i, max_j)
    if trace[max_i][max_j] == 'd':
        seq1_align.append(s1[max_i - 1])
        seq2_align.append(s2[max_j - 1])
        max_i -= 1
        max_j -= 1

    elif trace[max_i][max_j] == 'u':
        seq2_align.append(s2[max_j - 1])
        seq1_align.append('-')
        max_j -= 1

    else:
        seq1_align.append(s1[max_i - 1])
        seq2_align.append('-')
        max_i -= 1


print(seq1_align)
print(seq2_align)
