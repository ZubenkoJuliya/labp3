s = int(input())
a = set()
for i in range(s):
    x = input().split()
    for elem in x:
        a.add(elem)
print(len(a))
