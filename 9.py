result = {}
for i in range(int(input())):
    key, val = input().split()
    result[key] = result.get(key, 0) + int(val)

for key, val in sorted(result.items()):
    print(key, val)
