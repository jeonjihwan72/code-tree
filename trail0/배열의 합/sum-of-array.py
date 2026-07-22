result = [0 for _ in range(4)]

for i in range(4):
    temp = sum(map(int, input().split()))
    result[i] = temp

for answer in result:
    print(answer)