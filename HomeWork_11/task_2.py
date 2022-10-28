'''
Решить первую задачу используя итератор.
'''

class MyIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.first_number = 1
        self.second_number = 1
        self.sum_numbers = 0
        self.count = 2

    def __next__(self):
        if self.limit > 1:
            if self.count == 2:
                self.count -= 1
                return self.first_number
            elif self.count == 1:
                self.count -= 1
                return self.second_number
            self.sum_numbers = self.first_number + self.second_number
            self.first_number = self.second_number
            self.second_number = self.sum_numbers
            if self.sum_numbers <= self.limit:
                return self.sum_numbers
            else:
                raise StopIteration
        else:
            raise StopIteration

iter_fib = MyIterator(5000)

# print(next(iter_fib))
# print(next(iter_fib))
# print(next(iter_fib))
# print(next(iter_fib))
# print(next(iter_fib))
# print(next(iter_fib))

for i in iter_fib:
    print(i)




