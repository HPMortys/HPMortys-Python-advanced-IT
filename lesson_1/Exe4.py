# 4) Реализовать функцию bank, которая приннимает следующие
# аргументы: сумма депозита, кол-во лет, и процент. Результатом
# выполнения должна быть сумма по истечению депозита


def bank(sum_depo: int, age: int, percent: int):
    for i in range(age):
        sum_depo += sum_depo*percent/100
    return sum_depo

print(f'Sum : {bank(1555,2,5)}')
