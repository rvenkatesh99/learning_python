import argparse
import random
import sys

parser = argparse.ArgumentParser(
	description='Report how much of a genome is above the threshhold')
parser.add_argument('--size', required = True, type = int,
	metavar='<int>', help='genome size in bp')
parser.add_argument('--coverage', required = True, type = int,
	metavar='<int>', help='genome coverage level (1x, 2x, etc)')
parser.add_argument('--threshhold', required = True, type = int,
	metavar='<int>', help='threshhold completion desired per position')
parser.add_argument('--rl', required = False, default = 1, type = int,
	metavar='<int>', help='read length')

arg = parser.parse_args()

num_reads = arg.size * arg.coverage

# allocate genome
genome = []
for i in range(arg.size):
	#set all positions to 0
	genome.append(0)

for i in range(arg.size * arg.coverage):
	genome.append(0)
	# choose random positions within the genome
	rand_pos = random.randint(0, arg.size - 1)
	if arg.rl == 1:
		genome[rand_pos] += 1
	else:
		for curr_pos in range(rand_pos, rand_pos + arg.rl - 1):
			genome[curr_pos] += 1

thresh_counts = 0
for i in range(arg.size):
	if genome[i] <= arg.threshhold:
		thresh_counts += 1
above_thresh = (1 - thresh_counts/arg.size)*100

print(f'Genome size is {arg.size}.')
print(f'Coverage is {arg.coverage}X.')
print(f'Read length is {arg.rl} base pairs.')
print(f'Threshhold is {arg.threshhold}.')
print(f'The percentage of the genome that is above this threshold is {above_thresh}%.')
