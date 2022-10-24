n = int(input())
s = 0
p = 10 ** 9 + 7

if n % 2 == 0:
	s = 2
	for i in range(int(n / 2)):
		s *= 3
		while s > p:
			s -= p
else:
	s = 4
	for i in range(int((n - 1) / 2)):
		s *= 3
		while s > p:
			s -= p


print(s)