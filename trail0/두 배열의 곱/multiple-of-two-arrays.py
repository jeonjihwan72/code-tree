arr1 = [list(map(int, input().split())) for _ in range(3)]
space = input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

answer = [[arr1[i][j]*arr2[i][j] for j in range(3)] for i in range(3)]

for row in answer:
    for element in row:
        print(element, end=' ')
    print()