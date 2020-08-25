f = open("bruh.txt", 'r')

# print("every\nthing\n\nis\ngooooood!!!!!!!!!!!!!", file=f)

for char in f.read():
	print(char)

