from seqlib import read_fastq
import sys

for name, seq, qual in read_fastq(sys.argv[1]):
	print(name)

	for q in qual:
		qv = ord(q) - 33
		print(q, qv, 1/10**(qv/10))
