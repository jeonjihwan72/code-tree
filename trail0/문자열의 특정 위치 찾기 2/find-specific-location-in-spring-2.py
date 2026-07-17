words = ["apple", "banana", "grape", "blueberry", "orange"]

c = input()

answer = []

is_in_third_or_fourth = 0

for word in words:

    if len(word)>=3:
        if word[2] == c:
            is_in_third_or_fourth += 1
            answer.append(word)
            continue
    
    if len(word)>=4:
        if word[3] == c:
            is_in_third_or_fourth += 1
            answer.append(word)
            continue

for a in answer:
    print(a)

print(is_in_third_or_fourth)