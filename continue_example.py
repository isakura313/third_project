number = 0
while number < 15:
    number += 1
    if number % 3 == 0 or number % 5 == 0:
        continue
    else:
        print(number)
