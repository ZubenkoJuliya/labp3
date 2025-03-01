s1 = set()
s2 = set()

n = int(input())

k = 0
for i in range(n):
    sname = input()

    if not sname in s1:
        s1.add(sname)
        s2.add(sname)
    elif sname in s2:
        k += 2
        s2.remove(sname)
    else:
        k += 1

print(k)