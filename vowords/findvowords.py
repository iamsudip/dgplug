#!/usr/bin/env python

import argparse
import os
from sys import exit

vowels = ''
data = 'aeiouAEIOU'

def find_words(path, vowels):
    with open(str(path)) as fobj1:
        fobj = fobj1.read().split(' ')
        for word in fobj:
            if word[0] in data:
                if vowels == '':
                    print word
                if word[0] in vowels:
                    print word

parser = argparse.ArgumentParser(description = 'Finds words starting with a vowel')
parser.add_argument("-f", "--file", type = str,
                    help = "Path to file")
parser.add_argument("-v", "--vowel", type = str, 
                    help = "Find word starting with this particular vowel")
args = parser.parse_args()

if os.path.exists(args.file):
    if args.vowel:
        vowels = args.vowel
else:
    print "File does not exist"
    exit(-1)

find_words(args.file, vowels)
