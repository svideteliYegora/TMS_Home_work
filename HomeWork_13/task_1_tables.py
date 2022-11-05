'''
Необходимо создать таблицы 1 и 2 в вашей БД с помощью ORM Peewee. (Таблицы на диске)
'''

import peewee
from db_conection import db


class Basemodel(peewee.Model):
    class Meta:
        database = db


class Table1(Basemodel):
    part_id = peewee.AutoField()
    part = peewee.CharField(50)
    cat = peewee.IntegerField()


class Table2(Basemodel):
    catnumb = peewee.IntegerField()
    cat_name = peewee.CharField(50)
    price = peewee.FloatField()


Table1.drop_table()
Table2.drop_table()

Table1.create_table()
Table2.create_table()


# data for Table1
part_list = ["квартиры", "автомашины", "доски", "шкафы", "книги"]
cat_list = [505, 205, 10, 30, 160]

# data for Table2
catnumb_list = [10, 505, 205, 30, 45]
cat_name_list = ["стройматериалы", "недвижимость", "транспорт", "мебель", "техника"]
price_list = [105.00, 210.00, 160.00, 77.00, 65.00]

# cycle for fill Table1
for index, value in enumerate(part_list):
    Table1(part=value, cat=cat_list[index]).save()

# cycle for fill Table2
for index, value in enumerate(catnumb_list):
    Table2(catnumb=value, cat_name=cat_name_list[index], price=price_list[index]).save()



