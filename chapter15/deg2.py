L = [1, 2, 4, 8, 16, 32, 64]

x = 5

res = 2 ** x

for ind, i in enumerate(L):
	if res == i:
		print(f'at index {ind}')
		break
else:
	print(f'{x} not found')


if 2 ** x in L:
	print(f'at index {ind}')
else:
	print(f'{x} not found')	

list(map(lambda x: 2 ** x, raange(7)))