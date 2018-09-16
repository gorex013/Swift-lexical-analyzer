from src.keywords import keywords

def parseString(content):
	tokens = []

	def flush_token(substring, tokens):
		if len(substring) == 0:
			return
		token = keywords.get(substring, None)
		if token is not None:
			tokens.append(token)
		else:
			tokens.append({'IDENTIFIER': substring})

	substring = ''
	for i in content:
		if i == ' ':
			flush_token(substring, tokens)
			substring = ''
			continue
		substring += i
	flush_token(substring, tokens)

	return tokens

if __name__ == '__main__':
	equation = 'let a = b'
	tokens = parseString(equation)
	print(tokens)