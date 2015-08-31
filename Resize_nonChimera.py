#!/usr/bin/env python

# This script takes the usearch / uchime output and duplicates the sequences till the number of duplicates
# equals the amplicon size (indicated in the uchime header). Sequences are duplicated so that sequences
# are not labeled as singletons during clustering and the correct sequence number is displayed in the
# BLAST output.

# import the itertools and sys modules
import itertools, sys

# create a iterative index of all the headers
lines = (x[1] for x in itertools.groupby(open(sys.argv[1]), key=lambda line: line[0] == ">"))

# walk through the header and obtain the sequences (and quality score if applicable)
for headers in lines:

	# get the header, clust size and sequence
	header = headers.next().strip()
	size=int(header.split("size=")[1].split(";")[0])
	sequence = ''.join([line.strip() for line in lines.next()])

	# for each sequence in size: write a copy of the sequence
	for i in range(0,size):
		print '{0}\n{1}'.format(header, '\n'.join([sequence[i:i+60] for i in range(0, len(sequence), 60)]))

