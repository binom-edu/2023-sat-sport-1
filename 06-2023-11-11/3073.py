n = int(input())
z = 0
s = 0
while z != 2:
    if n != 0:
        s += n
        z = 0
    else:
        z += 1
    if z != 2:
        n = int(input())
print(s)