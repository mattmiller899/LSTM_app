#!/usr/bin/env python
# encoding: utf-8

import argparse

def seq2kmer(seqs, k, ext, dest):
    with open(seqs, 'r') as f:
        out = open(dest, 'w')
        if ext == "fasta":
            for num, line in enumerate(f):
                if num % 1000 == 0:
                    print('%d lines to n-grams' % num)
                if num % 2 == 0:
                    continue
                line = line[:-1].lower() # remove '\n' and lower ACGT
                l = len(line) # length of line
                for i in range(0, l-k+1):
                    out_line = "%s " % ''.join(line[i:i+k])
                    out.write(out_line)
                out.write('\n')
        else:
            for num, line in enumerate(f):
                if num % 1000 == 0:
                    print('%d lines to n-grams' % num)
                if num % 4 != 1:
                    continue
                line = line[:-1].lower() # remove '\n' and lower ACGT
                l = len(line) # length of line
                for i in range(0, l-k+1):
                    out_line = "%s " % ''.join(line[i:i+k])
                    out.write(out_line)
                out.write('\n')
    out.close()

def forglove(f, dest):
    f = open(f)
    with open(dest, 'w') as out:
        for num, line in enumerate(f):
            if num % 1000 == 0:
                print('%d lines saved' % num)
            out.write(line[:-1])
            out.write('none ' * 5)
    f.close()


