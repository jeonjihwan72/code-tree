N, M = map(int, input().split())

# Please write your code here.
while N > 0:
    print(N)
    # N //= M  <- 아래의 식과 수행 시간, 메모리가 동일함
    N = N // M