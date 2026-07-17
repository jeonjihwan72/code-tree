n = int(input())

answer = 0
step = 0

while True:
    if answer >= n:
        print(step)
        break
    step += 1
    answer += step

# for i in range(1, 101):
#     answer += i
#     if answer >= n:
#         print(i)
#         break