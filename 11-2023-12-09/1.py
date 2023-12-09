a = int(input())
b = int(input())

# Алгоритм Евклида для поиска НОД натуральных чисел

while a * b != 0:
    if a > b:
        a -= b
    else:
        b -= a
print(a + b)