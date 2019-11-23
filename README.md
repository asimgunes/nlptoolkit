# AsmFx NLPToolkit

AsmFx NLPToolkit is a set of Python command line scripts for basic NLP operations like cleaning and preparing data. 

## Script Files

AsmFx NLP Toolkit includes the following scripts:
* vocabulary.py

### 1. Creating Vocabulary from Corpus: vocabulary.py

vocabulary.py is a basic script for exporting vocabulary file from a given corpus. 

```
$> python vocabulary.py corpus.txt vocabulary.txt
``` 

Usage of the vocabulary.py file could be seen with -h or --help parameter.

```
$> python vocabulary.py --help
usage: vocabulary.py [-h] [--maxsize Max_Size] [--simple]
                     Corpus_File Vocabulary_File

positional arguments:
  Corpus_File         Corpus file to extract vocabulary
  Vocabulary_File     Vocabulary file name to save

optional arguments:
  -h, --help          show this help message and exit
  --maxsize Max_Size  Maximum vocabuary size to export
  --simple            Only export words without word counts
```

