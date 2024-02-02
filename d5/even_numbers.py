target = int(input()) #Enter a number between 0 and 1000

total = 0
if target <= 1000 or target > 0:
    if target == 100:
        for number in range(2, target+1):
            if number % 2 == 0:
                total += number
    else:
        for number in range(1, target+1):
            if number % 2 == 0:
                total += number

print(total)