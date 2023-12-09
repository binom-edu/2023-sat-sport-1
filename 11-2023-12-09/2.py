a = int(input())
b = int(input())

# Усовершенствованный алгоритм Евклида

while a * b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(a + b)