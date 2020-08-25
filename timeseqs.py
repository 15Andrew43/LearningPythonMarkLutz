import sys, mytimer

reps = 10000
replist = range(reps)

def forLoop():
	res = []
	for x in replist:
		res.append(x + 10)
	return res

def listComp():
	return [x + 10 for x in replist]

def mapCall():
	return list(map(lambda x: x + 10, replist))

def genExpr():
	return list(x + 10 for x in replist)

def genFunc():
	def gen():
		res = []
		for x in replist:
			yield x + 10
	return list(gen())

print(sys.version)

for test in (forLoop, listComp, mapCall, genExpr, genFunc):
	elapsed, result = mytimer.timer(test)
	print('-' * 33)
	print(f"{test.__name__} : {elapsed} => [{result[0]} ... {result[-1]}]")