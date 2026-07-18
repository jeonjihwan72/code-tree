n = int(input())

for i in range(1, n+1):
    row = [str(i) for _ in range(i)]
    row_string = " "
    print(row_string.join(row))