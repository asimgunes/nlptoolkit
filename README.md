# AsmFx NLPToolkit

AsmFx NLPToolkit is a set of Python command line scripts for basic NLP operations like normalizing and preparing data. 

## Script Files

AsmFx NLP Toolkit includes the following scripts:
* normalize.py
* vocabulary.py

### 1. Normalizing a Text File: normalize.py
With normalize.py a given input text file content can be normalized. Normalization process includes converting file to lower or upper case and replacing multiple whitespace to a single space. 

```
$> python normalize.py --lower --whitespace input.txt output.txt
```

Converting case of the text file depended for text language. Language could be defined by `--lang` parameters. Normalization script supports the following language parameters:

* en: English (default)
* tr: Turkish

For example, in order to normalize Turkish text file `--lang=tr` parameter could be passed in the command line.

```
$> python normalize.py --lower --whitespace --lang=tr input.txt output.txt
```

Usage of the normalize.py file could be seen with `-h` or `--help` parameter.

```
$> python normalize.py --help
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
```

### 2. Creating Vocabulary from Corpus: vocabulary.py

vocabulary.py is a basic script for exporting vocabulary file from a given corpus. 

```
$> python vocabulary.py corpus.txt vocabulary.txt
``` 

Usage of the vocabulary.py file could be seen with `-h` or `--help` parameter.

```
$> python vocabulary.py --help
usage: vocabulary.py [-h] [--maxsize Max_Size] [--simple]
                     Corpus_File Vocabulary_File

positional arguments:
  Corpus_File         Corpus file to extract vocabulary
  Vocabulary_File     Vocabulary file name to save

optional arguments:
  -h, --help          show this help message and exit
  --maxsize Max_Size  Maximum vocabulary size to export
  --simple            Only export words without word counts
```

