'''
Написать программу, которая будет создавать класс данных из JSON объекта.
(Дополнительно): Добавить метод для данного класса, который будет выводить все поля класса.
'''

import json

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35
}

with open('data.json', 'w') as write_file:
    json.dump(data, write_file)

with open('data.json') as read_file:
    json_data = json.load(read_file)

class MyClassJson:
    def getargs(self):
        print(f"name: {self.firstName}\n"
              f"lastName: {self.lastName}\n"
              f"hobbies: {self.hobbies}\n"
              f"age: {self.age}\n")

JsonData = type('JsonData', (MyClassJson,), json_data)
JsonDataObject = JsonData()
JsonDataObject.getargs()

