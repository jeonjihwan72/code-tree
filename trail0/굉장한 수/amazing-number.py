N = int(input())

great_num = "false"

if N%2 == 1 and N%3 == 0:
    great_num = "true"

if N%2 == 0 and N%5 == 0:
    great_num = "true"

print(great_num)