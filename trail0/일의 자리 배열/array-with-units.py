array = [0 for _ in range(10)]
array[0], array[1] = map(int, input().split())


for i in range(2, 10):
    array[i] = (array[i-1] + array[i-2])%10

for i in array:
    print(i, end=' ')