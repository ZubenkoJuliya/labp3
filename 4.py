s = [int(i) for i in input().split()]
p = set()
for i in s:
    if i in p:
        print('YES')
    else:
        print('NO')
    p.add(i)
