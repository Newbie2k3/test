 
n = int(input())
tong = 0
 
for i in range(1, n):
    if (n % i == 0):
        tong += i
 
if (tong == n):
    print(1)
else:
    print(0)