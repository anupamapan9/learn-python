my_numbers = [2, 4]


def avg(nums):
    i = 0
    leng = len(nums)

    for num in nums:
        i = i+num
    average = i/leng
    return average


total = avg(my_numbers)
print(total)
