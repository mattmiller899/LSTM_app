#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from preprocess import *
import argparse
import os
import sys

def get_args():
    parser = argparse.ArgumentParser(description='Generate n-grams and GloVe vectors')
    parser.add_argument('-k', dest='k', type=int, default=6, help='length of kmer')
    parser.add_argument('-s', dest='s', type=int, default=2, help='stride of splitting')
    parser.add_argument('-indir', dest='in_dir', help='directory where pos and neg are stored')
    parser.add_argument('-posname', dest='pos_name', help='name of pos file')
    parser.add_argument('-glove', dest='glove', help='whether to generate the 1-line corpus for GloVe') 
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    seq2ngram('%s/%s' % (args.in_dir, args.pos_name), args.k, args.s, '%s/%s_%dgram_%dstride' % (args.in_dir, args.pos_name, args.k, args.s))
    if args.glove:
        forglove('%s/%s_%dgram_%dstride' % (args.in_dir, args.pos_name, args.k, args.s),
                 '%s/%s_%dgram_%dstride_oneline' % (args.in_dir, args.pos_name, args.k, args.s))

if __name__ == "__main__":
    main()
