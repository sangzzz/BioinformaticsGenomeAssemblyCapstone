# import python3
import sys


def checkOptimal(n, reads):
    kmers = set()
    for read in reads:
        for i in range(0, len(read) - n + 1):
            kmers.add(read[i: i + n])
    prefixes = set()
    suffixes = set()
    for kmer in kmers:
        prefixes.add(kmer[:-1])
        suffixes.add(kmer[1:])
    return prefixes == suffixes


reads = []
for i in range(1618):
    read = sys.stdin.readline().strip()
    reads.append(read)

for n in range(len(reads[2]), 1, -1):
    if checkOptimal(n, reads):
        print(n)
        break
