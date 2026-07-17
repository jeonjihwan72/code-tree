N = int(input())
num_list = map(int, input().split())

result = []

for num in num_list:
    if num % 2 == 0:
        result.append(num)
        
# result.reverse()
result = result[::-1]

for answer in result:
    print(answer, end=" ")