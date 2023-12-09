a = int(input())
b = int(input())

# Алгоритм Евклида, 3 версия

while b != 0:
    a, b = b, a % b
print(a)