# Swift syntax analyzer
#### Implemented
```
1. imports
2. functions
3. cycles
4. if's
5. string and number literals
6. variables assignments
```

## BNF
```bnf
FunctionDeclaration::= func ID LP \[ID : Type\[, ID COLON Type\]* \] RP ARROW Type|(LP Type [, Type]+) RP LCP Expression RCP

FunctionCall::= ID LP \[Labeled|Const|FunctionCall \[, Labeled|Const|FunctionCall\]* \] RP  

Labeled ::= ID COLON Const  
Const ::= IntegerConst | StringConst  
IntegerConst ::= {'number': value}  
StringConst ::= {'multiline|inline string': value}  
Type ::= String | FLOAT | INTEGER | VOID | DOUBLE | ARRAY | DICT | CHARACTER | BOOL | UINT | SET  

Expression ::= ...  


If ::= 'if' ConditionList CodeBlock [ElseClause]
ElseClause ::= 'else' If | CodeBlock
ConditionList ::= Condition | Condition ',' ConditionList
Condition ::= Expression
CodeBlock ::= '{' Statements '}'
Statements ::= Statement | Statement Statements
Statement ::= ...

While ::= 'while' ConditionList CodeBlock

Repeat ::= 'repeat' CodeBlock 'while' Expression

For ::= 'for' ['case'] Pattern 'in' Collection CodeBlock
```
If you wish to take a look at FDeclaration & FCall PDAs - ask @evgerher

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
    -`lexer`
        - `preprocessing` directory
            - `comments.py` - methods for deleting comments from source code 
            - `escaping.py` - methods for escaping delimiters & operators, also it transform into final representation
            - `numeric_constants.py` - methods for parsing number values
            - `string_literals.py` - methods for processing string literals. Methods substitute the literal with TEMP# value. Such a way allows to keep it safe from later transformations
            - `swift_examples` directory
                - `BTree.swift` - BTree datastructure implemented of swift
                - `out.txt` - default out file
                - `lexical-analyzer.py`
                    - Main file for the lexer
                    - Provides args functionality & processes source code into list of tokens
                - `swift_tokens.py` - config file with dictionaries of token transformations
                    - `keywords`, `operators`, `delimiters`
                    - `operators_priority = ['<=', '>=', '+=', '-=', '*=', '/=', '%=', '+', '*', '*', '-', '/', '%', '>', '<']` - provides priority for processing operators.
                    - `string_literals['inline'] = 'INLINE_STRING_LITERAL'`
                    - `string_literals['multiline'] = 'MULTILINE_STRING_LITERAL'`
    -`syntaxer` syntax analyzer directory
        -`ObjectTrees.py` #todo
        -`grammars.py` #todo
        -`if-statement.py` file containig definitions of functions used for validating an if-statement. it is **triggered** by **'S_IF'** token. It return the 
        -`repeat-while` is not finished and is not working. The finction should be called when there's met the **'S_REAPEAT'** token. It yields the tree of the **repeat-statement** in form of a dictionary object.
        -`syntaxer` function that builds program tree
        -`test_funcs.txt` #todo
        -`test_lag.txt` #todo
        -`var_def.txt` #todo
        -`var_type.txt` #todo
        -`while_loop.py` in this file are contained the definition of the function that builds the tree of a **while-loop-statement**. The function is started when the syntaxer meets the **'S_WHILE'** token.
### test
- `tests.py` - python file with all the tests
    - `IdentifyComments` - tests methods for comments removal
    - `StringLiterals` - tests methods for substitution of string literals
    - `FormatTest` - tests lexical analysis
    
## Execution order
    A)Lexer
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
    B)Syntaxer
        1)Run the lexer and get the tokens' list
        2)Create tree object for every statement.
            1)Create trees for all if-statements
            2)Construct trees for all while-loop-statements
        3)
        4)
    
### Other mentions
1) Project was written in the beginning written in PyCharm, so `import` actions may become weird
2) In some places it is possible to optimize, but we are lazy
