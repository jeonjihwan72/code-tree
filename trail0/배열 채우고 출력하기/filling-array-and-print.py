input_list = input().split()

# for i in range(-1, -(len(input_list)+1), -1):
#     print(input_list[i], end='')

for i in range(len(input_list)):
    print(input_list[::-1][i], end='')