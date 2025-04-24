n = int(input())
a = []

for _ in range(n):
    inp = int(input())
    a.append(inp)

duplicate_found = False

for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            duplicate_found = True
            break
    if duplicate_found:
        break

if duplicate_found:
    print("YES")
else:
    print("NO")
