n = 3
arr = [[0 for y in range(n)] for x in range(n)]

y = 0
x = int(n/2)
arr[y][x] = 1

for i in range(2, n * n + 1):
    
	initial_y = y
	initial_x = x
	y = y - 1
	x = x + 1

	if y < 0:
		y = n - 1

	if x > n - 1:
		x = 0

	if arr[y][x] == 0:
		arr[y][x] = i
	else:
		y = initial_y + 1
		x = initial_x
		arr[y][x] = i


for i in range(n):
	for j in range(n):
		print("{0:5}".format(arr[i][j]), end="")
	print()