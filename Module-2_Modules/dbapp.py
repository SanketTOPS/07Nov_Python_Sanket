import read


def read(s):
	with open(s, encoding='utf-8') as f:
		return f.read()

s = read('foo.txt')
print(s)