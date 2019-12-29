#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Creates vocabulary file from given corpus file.
Author  : Asim Gunes
GitHub  : github.com/asimgunes
Date    : 23.11.2019
Version : 1.0

usage: vocabulary.py [-h] [--maxsize Max_Size] [--simple]
                     Corpus_File Vocabulary_File

positional arguments:
  Corpus_File         Corpus file to extract vocabulary
  Vocabulary_File     Vocabulary file name to save

optional arguments:
  -h, --help          show this help message and exit
  --maxsize Max_Size  Maximum vocabulary size to export
  --simple            Only export words without word counts
'''

from argparse import ArgumentParser

def getVocabulary(corpus):
    v = { }                                         # Initializing empty dictionary
    index = 0
    vsize = 0
    print('Reading corpus file: {}'.format(corpus))
    with open(args.corpus, 'r') as fp:              # Opening corpus
        for line in fp:                             # Reading corpus line by line
            index += 1
            for word in line.strip().split():       # Splitting line into words
                word = word.strip()                 #
                if word == '':                      # Omitting empty chunks
                    continue                        #
                elif word in v:                     # Increasing counter if word exists
                    v[word] = v[word] + 1           #
                else:                               # Adding word to dictionary if seen for the first time
                    v[word] = 1                     # 
                    vsize += 1
            if index % 10000 == 0:
                print('Reading corpus in line: {}, Vocabulary Size: {}'.format(index, vsize))
    print('Corpus completed. Total Lines: {}, Vocabulary Size: {}'.format(index, vsize))
    return v, vsize                                 # Returning the dictionary

def saveVocabulary(vocabulary, file, simple=False, sentunk=False,size=None):
    index = 0
    if(size):
        print('Exporting vocabulary to file: ', file, ', with MaxSize:', size)
    else:
        print('Exporting vocabulary to file: ', file)
    with open(args.vocabulary, 'w') as fp:                                  # Opening vocabulary file
        if(sentunk):
            fp.write('<S>\n')
            fp.write('</S>\n')
            fp.write('<UNK>\n')
            index += 3
        for k in sorted(vocabulary, key=vocabulary.get, reverse=True):      # Getting descending ordered vocabular list
            if simple:
                fp.write('{}\n'.format(k))                                  # Writing in simple format: only word
            else:
                fp.write('{} {}\n'.format(k,vocabulary[k]))                 # Writing word and word_count
            index += 1
            if index % 10000 == 0:
                print('Exporting vocabulary in line: ', index)
            if size is not None and index >= size:                          # Checking max export size
                break
    print('Vocabulary exported to file: ', file, ', Size:', index)

def main(args):
    v, vsize = getVocabulary(args.corpus)                                           # Get vocabulary dictionary
    saveVocabulary(v, args.vocabulary, simple=args.simple, size=args.maxsize)       # Save vocabulary dictionary file
    print('Operation completed succesfully.')

if __name__ == '__main__':
    # ArgumentParser configuration for user friendly command line usage
    parser = ArgumentParser(description='Creates vocabulary file from given corpus file.')
    parser.add_argument('corpus', metavar='Corpus_File', help='Corpus file to extract vocabulary')
    parser.add_argument('vocabulary', metavar='Vocabulary_File', help='Vocabulary file name to save')
    parser.add_argument('--maxsize', metavar='Max_Size', help='Maximum vocabulary size to export', type=int)
    parser.add_argument('--sentunk', help='Exports <S> </S> and <UNK>', action='store_true')
    parser.add_argument('--simple', help='Only export words without word counts', action='store_true')
    # Parsing arguments
    args = parser.parse_args()
    # Calling the main function
    main(args)