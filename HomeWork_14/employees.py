'''
2. Задачи:
-  Таблица Employees. Получить список всех сотрудников из 20го и из 30го отдела (department_id)
   <20й и 30й отделы заменю на 2й и 3й>
-  Таблица Employees. Получить список всех сотрудников с именем 'David'
-*  Таблица Employees. Получить список всех сотрудников которые пришли на работу в феврале 2021го года.
'''

from peewee import JOIN
from filling_tables import *


# Function which return list all employees
def get_list_func(obj):
    data = []
    for row in obj.tuples():
        data.append(row)
    return data


# Table Employees. Get list all employees from 2 and 3 departments
all_employees_depart = Empoloyees.select().where((Empoloyees.department_id == 2) | (Empoloyees.department_id == 3))
print(get_list_func(all_employees_depart))

# Table Employees. Get list all employees with name "David"
all_employees_davids = Empoloyees.select().where(Empoloyees.first_name == 'David')
print(get_list_func(all_employees_davids))

# Table Employees. Get list all employees, which came to work in February 2021.
all_february_employees = (Empoloyees.
                          select(Empoloyees).
                          join_from(Empoloyees,
                                    Job_history,
                                    join_type=JOIN.INNER,
                                    on=(Empoloyees.department_id == Job_history.department_id))
                          .where(Job_history.start_date.startswith('2021-02'))
                          )
print(get_list_func(all_february_employees))





