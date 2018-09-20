import keywords


def format(s):
    s = format_inline_comment(s)
    s = format_multiline_comment(s)
    s = delimiter_spacing(s)
    s = operator_spacing(s)
    s = keywords_replacement(s)
    return s


def format_multiline_comment(s):
    start = s.find('/*')
    while start != -1:
        end = s.find('*/')
        s = s.replace(s[start:end], ' ')  # todo: remove only first occurence
        start = s.find('/*')
    return s


def format_inline_comment(s):
    start = s.find('//')
    while start != -1:
        end = s[start:].find('\n')  # End in a substring from start index
        if end == -1:
            end = len(s)
        end = start + end + 1

        s = s.replace(s[start:end], ' ')  # TODO Does it do for all cases
        # s[start:end] = ' '
        start = s.find('//')
    return s


def delimiter_spacing(s):
    for key in keywords.delimiters.keys():
        s = s.replace(key, ' ' + keywords.delimiters[key] + ' ')
    return s


def operator_spacing(s):
    for key in keywords.operators.keys():
        s = s.replace(key, ' ' + keywords.operators[key] + ' ')
    return s


def keywords_replacement(s):
    for key in keywords.keywords.keys():
        s = s.replace(key, ' ' + keywords.keywords[key] + ' ')
    return s


# def parse(str=None):
print(format("""var a = 10 + 15 //k
var b=11 % 2 //k
func hello(x:Int)->Int
let x =131 //ewihfio
let `let` = 12
func hello(_ y:Int){
  print(y)
}
hello(`let`)"""))
