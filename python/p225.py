# 
# Solution to Project Euler problem 225
# 
# 

import itertools


def compute():
	INDEX = 123  # 0-based
	stream = (i for i in itertools.count(1, 2) if not has_tribonacci_multiple(i))
	ans = next(itertools.islice(stream, INDEX, None))
	return str(ans)


def has_tribonacci_multiple(i):
	seen = set()
	a, b, c = 1, 1, 1
	while True:
		if a % i == 0:
			return True
		key = (a, b, c)
		if key in seen:
			return False
		seen.add(key)
		a, b, c = b, c, (a + b + c) % i


if __name__ == "__main__":
	print(compute())
