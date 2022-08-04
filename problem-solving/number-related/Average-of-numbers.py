lent = int(input('How many numbers you want to enter: '))
total = 0
for i in range(lent):
    number = int(input('Enter number: '))
    total = number + total
print('Total Numbers is', total)
