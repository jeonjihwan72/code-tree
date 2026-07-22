color_map = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

input_map = [list(map(int, input().split())) for _ in range(4)]

total = 0

for i in range(4):
    for j in range(4):
        if color_map[i][j] == 1:
            total += input_map[i][j]

print(total)