# Swift lexical analyzer

## Team
- Vasile Rotaru @VMR013
- Evgeny Sorokin @evgerher

## Project specification
- python3
- unittest library

Program provides argparse functionality, use -h for help `python3 src/LexicalAnalyzer.py -h`
Example of program call `python3 src/LexicalAnalyzer.py src/swift_examples/BTree.swift src/swift_examples/out.txt`

## Project structure

### src
- `preprocessing` directory
    - `comments.py` - methods for deleting comments from source code 
    - `escaping.py` - methods for escaping delimiters & operators, also it transform into final representation
    - `numeric_constants.py` - methods for parsing number values
    - `string_literals.py` - methods for processing string literals. Methods substitute the literal with TEMP# value. Such a way allows to keep it safe from later transformations
- `swift_examples` directory
    - `BTree.swift` - BTree datastructure implemented of swift
    - `out.txt` - default out file
- `LexicalAnalyzer.py`
    - Main file for this project
    - Provides args functionality & processes source code into list of tokens
    - `swift_tokens.py` - config file with dictionaries of token transformations
        - `keywords`, `operators`, `delimiters`
        - `operators_priority = ['<=', '>=', '+=', '-=', '*=', '/=', '%=', '+', '*', '*', '-', '/', '%', '>', '<']` - provides priority for processing operators.
        - `string_literals['inline'] = 'INLINE_STRING_LITERAL'`
        - `string_literals['multiline'] = 'MULTILINE_STRING_LITERAL'`
### test
- `tests.py` - python file with all the tests
    - `IdentifyComments` - tests methods for comments removal
    - `StringLiterals` - tests methods for substitution of string literals
    - `FormatTest` - tests lexical analysis
    
## Execution order
1) Get rid of comments
2) Save string literals and substitute with TEMP#
3) Escape delimiters (transform and add spaces around)
4) Escape operators (transform and add spaces around)
    1) The order for 2 steps above matter, because `->` consists of `-` operator
5) Retrieve tokens list
    1) Split the content by spaces
    2) Transform each word into token
        1) Check is it already processed (step 3, 4)
        2) Check if it is a keyword
        3) Handle identifier
            1) Check if it is number and process
            2) Check if it is TEMP# and substitute back
            3) Else - substitute with `identifier: word`
            
### Other mentions
1) Project was written in the beginning written in PyCharm, so `import` actions may become weird
2) In some places it is possible to optimize, but we are lazy
