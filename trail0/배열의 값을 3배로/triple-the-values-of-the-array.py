answer = []

for _ in range(3):
    temp = list(map(int, input().split()))
    answer.append(temp)

for row in answer:
    for element in row:
        print(element*3, end=' ')
    print()