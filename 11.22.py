data = input().split()

for word in data:
    count = 0
    for item in data:
        if word == item:
            count += 1
    print(word, count)
