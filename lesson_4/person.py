from abc import ABC, abstractmethod
from datetime import date

date_ = date.today()


class Person(ABC):

    def __init__(self, surname, faculty, year_birth, month_birth, day_birth):
        self.surname = surname
        self.faculty = faculty
        self.year_birth = year_birth
        self.month_birth = month_birth
        self.day_birth = day_birth

    def define_age(self):
        return date_.year - self.year_birth - ((date_.month, date_.day) < (self.month_birth, self.day_birth))

    def find_person_in_range_age(start, end_, persons):
        print('--' * 20 + f'\nfrom {start} to {end_} years old: \n')
        for person in persons:
            age_person = person.define_age()
            if start <= age_person <= end_:
                print(f'{person.info_about_person()}Age: {age_person}\n')

    @abstractmethod
    def info_about_person(self):
        pass


class Entrant(Person):

    def info_about_person(self):
        return f'Entrant\n' \
               f'Surname: {self.surname}\n' \
               f'Faculty: {self.faculty}\n' \
               f'Data of birth: {self.year_birth}-{self.month_birth}-{self.day_birth}\n'


class Student(Person):
    def __init__(self, surname, faculty, year_birth, month_birth, day_birth, course):
        super().__init__(surname, faculty, year_birth, month_birth, day_birth)
        self.course = course

    def info_about_person(self):
        return f'Student\n' \
               f'Surname: {self.surname}\n' \
               f'Faculty: {self.faculty}\n' \
               f'Data of birth: {self.year_birth}-{self.month_birth}-{self.day_birth}\n' \
               f'Course: {self.course}\n'


class Teacher(Person):
    def __init__(self, surname, faculty, year_birth, month_birth, day_birth, post, experience):
        super().__init__(surname, faculty, year_birth, month_birth, day_birth)
        self.post = post
        self.experience = experience

    def info_about_person(self):
        return f'Teacher\n' \
               f'Surname: {self.surname}\n' \
               f'Faculty: {self.faculty}\n' \
               f'Data of birth: {self.year_birth}-{self.month_birth}-{self.day_birth}\n' \
               f'Post: {self.post}\n' \
               f'Experience: {self.experience}\n'


persons = [Entrant('Klock', 'FISP', 2000, 9, 29), Entrant('Ritm', 'FOD', 2001, 9, 26),
           Teacher('Halo', 'FOD', 1991, 4, 13, 'Assistant', '2 years'), Student('Nick', 'FOD', 2000, 5, 19, '2 course')]

for person in persons:
    print(person.info_about_person())

start = int(input('Enter start value of age range: '))
end_ = int(input('Enter last value of age range: '))
Person.find_person_in_range_age(start, end_, persons)
