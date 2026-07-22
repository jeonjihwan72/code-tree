n = int(input())

target = [i for i in range(1,n+1)]

result = []

for _ in range(n):
    # result.append(target[:])
    # result.append(target)
    result.append(target.copy())
    target = target[::-1]

    # result.append(target[:])
    # target.reverse()

for row in result:
    for element in row:
        print(element, end='')
    print()