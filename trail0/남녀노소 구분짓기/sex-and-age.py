gender = int(input())
age = int(input())

if gender == 0:
    # 남자인 경우
    if age >= 19:
        # 성인인 경우
        print("MAN")
    else:
        # 미성년자인 경우
        print("BOY")
else:
    # 여자인 경우
    if age >= 19:
        # 성인인 경우
        print("WOMAN")
    else:
        # 미성년자인 경우
        print("GIRL")
