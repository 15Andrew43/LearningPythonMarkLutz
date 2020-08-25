def countLines(file):
	return len(file.readlines())

def countChars(file):
	return len(file.read())

def test(name):
	with open(name) as file:
		print(f'lines : {countLines(file)}')
		file.seek(0)
		print(f'chars : {countChars(file)}')


if __name__ == '__main__':
	import mymod
	print(type(mymod.__name__))
	test(mymod.__name__ + '.py')

print('------------------------------------\n\n\n')