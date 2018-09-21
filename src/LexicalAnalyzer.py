from src.swift_tokens import *
import src.preprocessor as ps

def format(source):
    with open(source) as f:
        content = f.read()
    comments_filtered = ps.preprocess_src(content)
    tokens_string = keywords_replacement(comments_filtered)
    tokens_list = extract_tokens(tokens_string)
    return tokens_list

def extract_tokens(tokens_string: str) -> list:
    words = tokens_string.split(' ')

def keywords_replacement(s):
    for key in keywords.keys():
        s = s.replace(key, ' ' + keywords[key] + ' ')
    return s


if __name__ == '__main__':
    print(format("""var a = 10 + 15 //k
    var b=11 % 2 //k
    func hello(x:Int)->Int
    let x =131 //ewihfio
    let `let` = 12
    func hello(_ y:Int){
      print(y)
    }
    hello(`let`)"""))
