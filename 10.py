l1 = []
l2 = []
n = int(input())
for line in range(n):
    line = input().split()
    line = ['read' if x == 'R' else x for x in line]
    line = ['write' if x == 'W' else x for x in line]
    line = ['execute' if x == 'X' else x for x in line]
    l1.append(line)
m = int(input())
for l in range(m):
    l = input().split()
    l[0], l[1] = l[1], l[0]
    l2.append(l)
for j in range(m):
    for i in range(n):
        if l1[i][0] == l2[j][0]:
            if l2[j][1] in l1[i][1:]:
                print('OK')
            if l2[j][1] not in l1[i][1:]:
                print('Access denied')
