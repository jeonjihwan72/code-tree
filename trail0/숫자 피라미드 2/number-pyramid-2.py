n = int(input())

current = 0

for i in range(1, n+1):
    for j in range(i):
        current += 1
        print(current, end=' ')
    print()