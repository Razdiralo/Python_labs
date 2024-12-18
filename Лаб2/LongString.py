strings = input("Введите строки через запятую: ").split(", ")
max_length = max(len(s) for s in strings)
print(f"Длина самой длинной строки: {max_length}")
