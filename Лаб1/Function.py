import math

def f(x):
    return x**2

def calculate_a(x, y):
    if x * y > 0:
        result = (f(x) + y)**2 - math.sqrt(f(x) * y)
    elif x * y < 0:
        result = (f(x) + y)**2 + math.sqrt(abs(f(x) * y))
    else:
        result = (f(x) + y)**2 + 1
    return result

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

a = calculate_a(x, y)
print(f"Результат a: {a}")
