s = sorted(list(set([int(s) for s in input().split()]) & set([int(s) for s in input().split()])))
for elem in s:
    print(elem, end=' ')
