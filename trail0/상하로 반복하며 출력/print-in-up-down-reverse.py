n = int(input())

result_map = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            result_map[j][i] = j+1
    else:
        for j in range(n):
            result_map[j][i] = n-j

for row in result_map:
    for element in row:
        print(element, end='')
    print()