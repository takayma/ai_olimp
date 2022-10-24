from math import exp, log
from random import uniform

a = int(input())

def f(x):
	return 1 / (1 + exp(-x))

def df(x):
	return (1 - x) * x

def loss(ideal, output):
	return (ideal - output) ** 2

k = [1, 2, 1]
w = [[[uniform(-1, 1) for _1 in range(k[i + 1])] for _2 in range(k[i] + 1)] for i in range(len(k) - 1)]
delta_w = [[[0 for _1 in range(k[i + 1])] for _2 in range(k[i] + 1)] for i in range(len(k) - 1)]
n = 0.7
m = 0.5

def forward_fc(data_input):
	x = [[0 for _1 in range(k[i])] for i in range(len(k))]
	x[0] = [data_input]
	for i in range(len(x) - 1):
		x[i].append(1)

	for i in range(len(k) - 1):
		for j in range(k[i + 1]):
			for d in range(k[i] + 1):
				x[i + 1][j] += x[i][d] * w[i][d][j]
			x[i + 1][j] = f(x[i + 1][j])

	return x

def backpropagation_fc(data_output):
	err = [[0 for _1 in range(k[i])] for i in range(len(k))]
	err[-1][0] = loss(data_output, x[-1][0]) * df(x[-1][0])

	for i in range(len(k) - 2, 0, -1):
		for j in range(k[i]):
			for d in range(k[i + 1]):
				err[i][j] += err[i + 1][d] * w[i][j][d] * df(x[i][j])

	for i in range(len(k) - 1):
		for j in range(k[i + 1]):
			for d in range(k[i] + 1):
				delta_w[i][d][j] = m * delta_w[i][d][j] - n * x[i][d] * err[i + 1][j]
				w[i][d][j] += delta_w[i][d][j]

	return delta_w, w, err

for i in range(1000):
	x = forward_fc(n)
	delta_w, w, err = backpropagation_fc(18)

inp = int(input())
print(forward_fc(inp))