N = int(input("Введите число N: "))
even_sum = sum(i for i in range(2, N+1, 2))
print(f"Сумма всех чётных чисел от 1 до {N}: {even_sum}")
