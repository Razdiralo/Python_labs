N = int(input("Введите число N: "))
fib = [0, 1]
while fib[-1] + fib[-2] <= N:
    fib.append(fib[-1] + fib[-2])
print("Числа Фибоначчи до числа N:", fib)
