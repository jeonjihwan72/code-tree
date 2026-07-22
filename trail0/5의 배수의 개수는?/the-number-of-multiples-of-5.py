map_input = []

for _ in range(4):
    temp_list = list(map(int, input().split()))
    map_input.append(temp_list)

cnt = 0

for i in range(4):
    for j in range(4):
        if map_input[i][j] % 5 == 0:
            cnt += 1

print(cnt)