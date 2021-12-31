from math import ceil
m, n, a = [int(x) for x in input().split()]
m1 = ceil(m/a)
n1 = ceil(n/a)
print(m1*n1)