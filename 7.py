s = {}
for w in input().split():
    s[w] = s.get(w, 0) + 1
    print(s[w] - 1, end=' ')
