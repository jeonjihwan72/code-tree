s_1, s_2 = input().split()

if len(s_1) > len(s_2):
    print(s_1, len(s_1))
elif len(s_1) == len(s_2):
    print("same")
else:
    print(s_2, len(s_2))