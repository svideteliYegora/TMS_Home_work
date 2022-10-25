'''
Напишите программу с классом Student, в котором есть четыре атрибута: firstName, lastName, groupNumber и age.
Установить им любые значения по умолчанию. Необходимо создать пять методов: getFullName, getAge, getGroupNumber,
setNameAge, setGroupNumber. Метод getFullName нужен для получения данных об полном имени конкретного студента,
метод getAge нужен для получения данных о возрасте конкретного студента, метод GetGroupNumber нужен для получения
данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных
по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. В программе необходимо
создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.
'''

class Student:
    first_name = 'Greg'
    last_name = 'Wilson'
    group_number = 5
    age = 19

    def get_full_name(self):
        print(self.first_name, self.last_name)

    def get_age(self):
        print(self.age)

    def get_group_number(self):
        print(self.group_number)

    def set_name_age(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def set_group_number(self, group_number: int):
        self.group_number = group_number

# first instance class Student
object1 = Student()
object1.set_name_age(first_name='Carl', last_name='Marks', age=25)
object1.set_group_number(group_number=4)

# second instance class Students
object2 = Student()
object2.set_name_age(first_name='John', last_name='Doe', age=33)
object2.set_group_number(group_number=6)

# third instance class Students
object3 = Student()
object3.set_name_age(first_name='Steve', last_name='Jobs', age=41)
object3.set_group_number(group_number=1)

# fourth instance class Students
object4 = Student()
object4.set_name_age(first_name='Tonny', last_name='Montana', age=29)
object4.set_group_number(9)

# fifth instance class Students
object5 = Student()
object5.set_name_age(first_name='Bob', last_name='Marley', age=35)
object5.set_group_number(2)
