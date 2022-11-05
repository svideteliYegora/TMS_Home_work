'''
Реализовать такую функцию в Python с помощью ORM Peewee.  (До следующего понедельника)
'''

from peewee import *
from db_conection import db
from task_1_tables import *


# function convert object <class 'peewee.ModelSelect'> to the object <class 'tuple'> and print it.
def print_func(obj):
    for row in obj.tuples():
        print(row)
    print()


# INNER JOIN
inner_join_query = (Table1
                    .select(Table1, Table2)
                    .join_from(Table1, Table2, join_type=JOIN.INNER, on=(Table1.cat == Table2.catnumb))
                    )
print_func(inner_join_query)

# LEFT JOIN
left_join_query = (Table1
                   .select(Table1, Table2)
                   .join_from(Table1, Table2, join_type=JOIN.LEFT_OUTER, on=(Table1.cat == Table2.catnumb))
                   )
print_func(left_join_query)

# LEFT JOIN... WHERE...
left_join_w_query = (Table1
                     .select(Table1, Table2)
                     .join_from(Table1, Table2, join_type=JOIN.LEFT_OUTER, on=(Table1.cat == Table2.catnumb))
                     .where(Table2.catnumb.is_null())
                     )
print_func(left_join_w_query)

# RIGHT JOIN
right_join_query = (Table1
                    .select(Table1, Table2)
                    .join_from(Table1, Table2, join_type=JOIN.RIGHT_OUTER, on=(Table1.cat == Table2.catnumb))
                    )
print_func(right_join_query)

# RIGHT JOIN... WHERE...
right_join_w_query = (Table1
                      .select(Table1, Table2)
                      .join_from(Table1, Table2, join_type=JOIN.RIGHT_OUTER, on=(Table1.cat == Table2.catnumb))
                      .where(Table1.cat.is_null())
                      )
print_func(right_join_w_query)

# FULL OUTER JOIN
full_join_query = ((Table1
                    .select(Table1, Table2)
                    .join_from(Table1, Table2, join_type=JOIN.LEFT_OUTER, on=(Table1.cat == Table2.catnumb)))
                   |
                   (Table1
                    .select(Table1, Table2)
                    .join_from(Table1, Table2, join_type=JOIN.RIGHT_OUTER, on=(Table1.cat == Table2.catnumb)))
                   )
print_func(full_join_query)

# FULL OUTER JOIN... WHERE...
full_join_w_query = ((Table1
                      .select(Table1, Table2)
                      .join_from(Table1, Table2, join_type=JOIN.LEFT_OUTER, on=(Table1.cat == Table2.catnumb)))
                     .where(Table2.catnumb.is_null())
                     |
                     (Table1
                      .select(Table1, Table2)
                      .join_from(Table1, Table2, join_type=JOIN.RIGHT_OUTER, on=(Table1.cat == Table2.catnumb)))
                     .where(Table1.cat.is_null())
                     )
print_func(full_join_w_query)
