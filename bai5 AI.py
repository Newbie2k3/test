from collections import Counter
count = Counter()
#n = int(input())
a = input().split()

n = int(a[0])
for i in range(1,n+1):
    doi = a[i]
    count[doi] = count.get(doi, 0) + 1
win = count.most_common(1)
print(win[0][0])

