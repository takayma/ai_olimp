n = int(input())
if n % 2 == 0:
	n = n >> 1
	print(int(n))
else:
	print(0)