JSON to JSON diff tool
=================

##Introduction

A module for checking equivalence and difference of two JSONs with regex support

This repository will treat two types of JSON necessary for our purpose:

1. Regular JSON where only data is stored

2. Model JSON which will treat all keys and values as regular expressions
    * Models will be used for comparing JSON objects to A model for 
        equivalence with regex matching
    * As JSON can be in a non-deterministic order, this is harder 
        than doing a straight string comparison
    
###There are four modes of this module

1. Regular JSON comparison
2. JSON to Model comparison
3. Regular JSON diff
4. JSON to Model Diff

##1. Regular JSON comparison
This simply tests whether two files contating json are the same
```bash
./json_diff.py path/to/file1.json path/to/file2.json
```
Returns True if equal or False otherwise.

```bash
.json_diff.py path/to/file1.json path/to/json_directory/
```
Returns first match if there is one, or False otherwise.



##Command Line Usages

To do a json to model comparison (regex support):
```bash
./json_diff.py -m j2m path/to/pure.json path/to/regex.json
```

