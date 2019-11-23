#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Normalizes input file and write normalized file to output file.
Author  : Asim Gunes
GitHub  : github.com/asimgunes
Date    : 23.11.2019
Version : 1.0

usage: normalize.py [-h] [--lang Language] [--lower] [--upper] [--whitespace]
                    Input_File Output_File

positional arguments:
  Input_File       Input file to normalize
  Output_File      Output file after normalize

optional arguments:
  -h, --help       show this help message and exit
  --lang Language  Normalize in language [en, tr]
  --lower          Convert content to lower
  --upper          Convert content to upper
  --whitespace     Replace multiple whitespace to single space

'''

from argparse import ArgumentParser


def normalizeCommon(text, args):
    if(args.whitespace):
        text = ' '.join(text.strip().split())+ '\n'
    return text

def normalizeTR(text, args):
    text = normalizeCommon(text, args)
    if(args.lower):
        text = text.replace('İ', 'i').replace('I', 'ı').replace('Ğ', 'ğ').replace('Ü', 'ü').replace('Ş', 'ş').replace('Ö', 'ö').replace('Ç', 'ç').lower()
    elif(args.upper):
        text = text.replace('i', 'İ').replace('ı', 'I').replace('ğ', 'Ğ').replace('ü', 'Ü').replace('ş', 'Ş').replace('ö', 'Ö').replace('ç', 'Ç').upper()
    return text

def normalizeEN(text, args):
    text = normalizeCommon(text, args)
    if(args.lower):
        text = text.lower()
    elif(args.upper):
        text = text.upper()
    return text

def normalize(input_file, output_file, normalizeFunc, args):
    with open(input_file, 'r') as input_fp:
        with open(output_file, 'w') as output_fp:
            for line in input_fp:
                output_fp.write(normalizeFunc(line, args))

def main(args):
    languages = {'en':normalizeEN, 'tr':normalizeTR}
    normalizeFunc = normalizeEN
    if(args.lang and args.lang in languages):
        normalizeFunc = languages[args.lang]

    normalize(args.input, args.output, normalizeFunc, args)   # Normalize 
    print('Operation completed succesfully.')

if __name__ == '__main__':
    # ArgumentParser configuration for user friendly command line usage
    parser = ArgumentParser(description='Normalizes input file and write normalized file to output file.')
    parser.add_argument('input', metavar='Input_File', help='Input file to normalize')
    parser.add_argument('output', metavar='Output_File', help='Output file after normalize')
    parser.add_argument('--lang', metavar='Language', help='Normalize in language [en, tr]')
    parser.add_argument('--lower', help='Convert content to lower', action='store_true')
    parser.add_argument('--upper', help='Convert content to upper', action='store_true')
    parser.add_argument('--whitespace', help='Replace multiple whitespace to single space', action='store_true')
    # Parsing arguments
    args = parser.parse_args()
    # Calling the main function
    main(args)