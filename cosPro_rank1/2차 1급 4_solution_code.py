num = 123
k = 0
while num > 0:
    k %= 10
    num //= 10
    print(k)