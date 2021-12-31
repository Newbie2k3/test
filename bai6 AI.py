from math import ceil
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
n = int(input())
if (n >= ceil(sum(a)/5) + ceil(sum(b)/10) ):
    print("YES")
else : print("NO")
