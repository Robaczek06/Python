import random


def BubbleSort(sort_nums):
    for i in range(100):
        sort_nums.append(random.randint(1, 1000))

    for i in range(len(sort_nums)):
        for j in range(len(sort_nums)-i-1):
            if sort_nums[j] > sort_nums[j+1]:
                sort_nums[j], sort_nums[j+1] = sort_nums[j+1], sort_nums[j]

    for i in range(100):
        print(sort_nums[i], end=", ")


random_numbers = []
BubbleSort(random_numbers)
