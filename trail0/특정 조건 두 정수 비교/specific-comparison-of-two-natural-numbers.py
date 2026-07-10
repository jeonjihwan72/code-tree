a, b = map(int, input().split())

result = [1 if a<b else 0, 1 if a==b else 0]

for r in result:
    print(r, end=' ')