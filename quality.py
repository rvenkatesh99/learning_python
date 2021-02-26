qvalues = [
    [20, 30, 40, 23, 35, 15, 22],
    [20, 25, 30, 35, 20, 20, 18],
    [30, 25, 20, 15, 28, 10, 31]
]

# qvalues[1].append('hello')
# print(qvalues[1][7]) # 2 dimensional
# print(qvalues[1][7][1]) # iterate through chars in hello; 3 Dimensions
#
# for qvs in qvalues:
#     sum = 0
#     for qv in qvs:
#         sum += qv
#     print(sum)

# summing by columns:
length = len(qvalues[0])
for i in range(length):
    sum = 0
    for row in qvalues:
        sum += row[i]
    print(i, sum, sum/len(qvalues))
# sum is average quality value at each position
