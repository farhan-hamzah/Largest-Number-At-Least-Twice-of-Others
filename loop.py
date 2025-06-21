a = list(map(int, input().split()))
max_val = a[0]
idx = 0
for i in range(len(a)):
    if a[i] > max_val:
        max_val = a[i]
        idx = i
is_valid = True
for i in range(len(a)):
    if i != idx and max_val < 2 * a[i]:
        is_valid = False
        break

if is_valid:
    print(max_val)
else:
    print(-1)
