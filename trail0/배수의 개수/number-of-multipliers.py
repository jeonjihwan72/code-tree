three_cnt = 0
five_cnt = 0

for _ in range(10):
    target = int(input())

    if target % 3 == 0:
        three_cnt += 1
    
    if target % 5 == 0:
        five_cnt += 1
    
print(three_cnt, five_cnt)