s = input()
l = len(s) - 1
answer = 1

while l > 0:
	i = 0
	while i < len(s) - l:
		if s[i] == s[i + l]:
			answer = l + 1
			l = 1
			break
		i += 1
	l -= 1

print(answer)