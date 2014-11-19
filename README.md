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
    
The progression of development will be:

- [x] Equivalence of regular JSON

- [x] Comparison of regular JSON to a model JSON file
    
- [x] Equivalence of JSON file to a list of models
   - This can be used for classification purposes

- [x] Diff tool of regular JSON
   - Known issue handling deletions from list, possibly fixed by 2-pass diff

- [x] Diff tool or regular JSON compared to a model JSON file
   - This tool supports regexes for only leaves in the JSON structure for simplification


##Command Line Usages
To do an json to json comparison (default behavior):
```bash
./json_diff.py path/to/file1.json path/to/file2.json
```
To do a json to model comparison (regex support):
```bash
./json_diff.py -m j2m path/to/pure.json path/to/regex.json
```

