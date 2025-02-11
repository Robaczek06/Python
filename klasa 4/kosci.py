import random


def randomizer(dices_num):
    return [random.randint(1, 6) for i in range(dices_num)]


def points_counter(dice_values):
    points = 0
    for i in range(7):
        tempcounter = sum(1 for value in dice_values if value == i)
        if tempcounter >= 2:
            points += tempcounter * i
    return points


while True:
    while True:
        dices = int(input("Ile chcesz rzucić kostek? (3-10): "))
        if 3 <= dices <= 10:
            break

    numbers = randomizer(dices)
    for i, number in enumerate(numbers, start=1):
        print(f"Kostka {i}: {number}")

    points = points_counter(numbers)
    print(f"liczba uzyskanych punktów: {points}")

    answer = input("czy chcesz rzucić jeszcze raz? (t/n): ")
    if answer.lower() == 'n':
        break
    elif answer.lower() == 't':
        continue
    else:
        print('zła wartość')
        break
