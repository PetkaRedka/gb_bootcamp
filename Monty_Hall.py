from random import randrange, choice

from sympy import false, true


def monty_hall(door_num, change_choice):

    doors = {1, 2, 3}
    right_door = randrange(1,4)

    # Исключаем заведомо известную неверную дверь
    # Эта часть вообще не нужна, но она наглядно показывает,
    # почему далее именно такие условия
    wrong_door = doors.difference({door_num, right_door})
    if len(wrong_door) == 2:
        wrong_door.pop()
    doors.difference_update(wrong_door)

    # Учитываем выбор
    if change_choice == true:
        if right_door == door_num:
            return false
        else:
            return true

    else:
        if right_door == door_num:
            return true
        else:
            return false

win_counter_change_choise = 0
win_counter_const = 0

for i in range(0, 1000):
    if monty_hall(randrange(1,4), false):
        win_counter_const += 1

for i in range(0, 1000):
    if monty_hall(randrange(1,4), true):
        win_counter_change_choise += 1

print("Без смены: ", win_counter_const)
print("Со сменой: ", win_counter_change_choise)