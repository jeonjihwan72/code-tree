n = int(input())

answer = 0

# for i in range(1, n+1):
#     if (i%2!=0) and (i%3!=0) and (i%5!=0):
#         answer += 1

for i in range(1, n+1):
    if i%2==0:
        continue
    if i%3==0:
        continue
    if i%5==0:
        continue
    answer += 1

print(answer)