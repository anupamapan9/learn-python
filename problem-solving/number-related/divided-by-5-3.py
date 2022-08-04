def devisable_by_3and5(num):
    result = []
    for i in range(num):
        if i % 5 == 0 and i % 3 == 0:
            result.append(i)
    return result


numbers = int(input('Enter Your number: '))
print(devisable_by_3and5(numbers))
