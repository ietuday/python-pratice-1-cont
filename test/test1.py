from collections import defaultdict

n = int(input().strip())
c = map(int, input().strip().split(' '))

d = defaultdict(int)
for k in c:
    d[k] += 1

cnt = 0
for ele in d.values():
    cnt += ele//2

print(cnt)
