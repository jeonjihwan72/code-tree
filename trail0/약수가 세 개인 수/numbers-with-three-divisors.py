start, end = map(int, input().split())

# Please write your code here.

answer = 0

for num in range(start, end+1):
    div_cnt = 0
    for div_target in range(1, num+1):
        if num % div_target == 0:
            div_cnt += 1
        
        if div_cnt >= 4:
            break
    
    if div_cnt == 3:
        answer += 1

print(answer)