# Создать декоратор, который принимает на вход аргумент «количество
# повторений». Который будет вызывать функцию, определенное кол-во
# раз. Декорируемая функция должна возвращать:
# 1) Количество времени затраченное на каждый вызов;
# 2) Количество времени затраченное в общей сложности на все
# вызовы;
# 3) Имя декорируемой функции;
# 4) Значение последнего результата выполнения.

import time
import random


def decorator(count,test):
    def actual_decorator(func):
        def wrapper():
            print(test)
            sum_time, res = 0, None
            info_dict = {}
            info_dict['Name of func'] = func.__name__
            for i in range(count):
                time_start = time.time()
                res = func(test)
                time_end = time.time()
                sum_time += round(time_end - time_start, 9)
                info_dict[f'{i + 1} call'] = time_end - time_start
            info_dict['total time'], info_dict['last result of func'] = sum_time, res
            return info_dict

        return wrapper

    return actual_decorator


@decorator(5,1000)
def rand_sumator(test):
    return sum(range(random.randint(test, 100000)))

print(rand_sumator())
