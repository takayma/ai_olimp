n, m, a, b = map(int, input().split())
d = [list(map(int, input().split())) for _1 in range(n)]
maxx = 0

for p in range(a - 1, -1, -1):
	for q in range(b - 1, -1, -1):
		for r in range(a - 1, n):
			for s in range(b - 1, m):
				x = d[p][q] + d[r][s] + 2 * (r - p + 1 + s - q + 1)
				maxx = max(maxx, x)
				#print(p, q, r, s, x, maxx)

print(maxx)