# 1)Создать список из N элементов (от 0 до n с шагом 1).
# В этом списке вывести все четные значения.
N = int(input('Enter number of elements(N): '))
lt_num = list(range(N+1))
print(*[i for i in lt_num if i%2 == 0])
