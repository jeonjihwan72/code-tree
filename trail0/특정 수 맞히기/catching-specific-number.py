while True:
    input_number = int(input())
    if input_number == 25:
        print("Good")
        break
    elif input_number > 25:
        print("Lower")
    else:
        print("Higher")