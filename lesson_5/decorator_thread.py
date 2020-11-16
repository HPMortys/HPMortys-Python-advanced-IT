# 1) Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.
from threading import Thread
import time


def decorator(name_thread: str, demon: bool):
    def actual_decorator(func):
        def wrapper(arg):
            thr = Thread(target=func, args=(arg,))
            thr.setName(name_thread)
            thr.daemon = demon
            print(f'Thread {thr.getName()}')

            thr.start()
        return wrapper

    return actual_decorator


@decorator('T1', False)
def func_for_thred(seconds):
    print('Thread is starting')
    print(f'Slleeping for {seconds} sec')
    time.sleep(seconds)
    print('Thread is finishing')


sec = int(input('Enter how much seconds: '))

func_for_thred(sec)

