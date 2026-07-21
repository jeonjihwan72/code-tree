n, m = map(int, input().split())

arr1 = []
arr2 = []

for _ in range(n):
    temp = list(map(int, input().split()))
    arr1.append(temp)

for _ in range(n):
    temp = list(map(int, input().split()))
    arr2.append(temp)

answer = [[0 for _ in range(m)] for _ in range(n)]

for i in range(0, n):
    for j in range(0, m):
        if arr1[i][j] != arr2[i][j]:
            answer[i][j] = 1

for row in answer:
    for element in row:
        print(element, end=' ')
    print()