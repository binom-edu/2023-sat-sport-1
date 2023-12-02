n = int(input())
m = int(input())
s = int(input())
p = int(input())
tot = n * (m * 60 + s) + (n - 1) * p
print(tot // 60)
print(tot % 60)
