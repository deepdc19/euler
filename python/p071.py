# 
# Solution to Project Euler problem 71
# 
# 

import sys
if sys.version_info.major == 2:
	range = xrange


def compute():
	maxnumer = 0
	maxdenom = 1
	for d in range(2, 1000001):
		n = d * 3 // 7
		if d % 7 == 0:
			n -= 1
		if n * maxdenom > d * maxnumer:
			maxnumer = n
			maxdenom = d
	return str(maxnumer)


if __name__ == "__main__":
	print(compute())
