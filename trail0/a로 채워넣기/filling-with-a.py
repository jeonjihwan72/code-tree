temp = list(input())

temp[-2], temp[1] = 'a', 'a'

answer = "".join(temp)

print(answer)