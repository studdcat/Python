def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("f(1):", fibonacci(1))
print("f(2):", fibonacci(2))
print("f(3):", fibonacci(3))
print("f(4):", fibonacci(4))
print("f(5):", fibonacci(5))
