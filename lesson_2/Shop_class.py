# 2) Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.

class Shop:
    """Class Shop"""

    sum_of_sale = 0

    def __init__(self, name, sale_amount):
        self.name = name
        self.sale_amount = sale_amount
        self.sum_of_sale += sale_amount

    def enlarge_sale(self):
        num_sale = int(input('Введите на сколько увеличилось кол-во проданных товаров: '))
        self.sum_of_sale += num_sale
        self.sale_amount = self.sale_amount + num_sale
        print(f'Кол-во проданных товаров {self.sale_amount}')

    def show_Sum(self):
        print(f'Общее кол-во товаров проданных всеми магазинами {self.sum_of_sale}')


mag1 = Shop('Candy',200)
mag1.enlarge_sale()
mag1.show_Sum()
