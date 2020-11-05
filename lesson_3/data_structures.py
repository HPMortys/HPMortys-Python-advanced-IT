class Data_Structures():
    def __init__(self,lt_data: list):
        self._lt_data = lt_data

    def add_new_elment(self):
        new_elem = int(input("Enter new element: "))
        self._lt_data.append(new_elem)

    def get_elements(self):
        print(*self._lt_data)

lt_data = [1,2,3,4,5]

data = Data_Structures(lt_data)
data.add_new_elment()
data.get_elements()



