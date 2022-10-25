'''
Выберете любую папку на своем компьютере, имеющую вложенные директории. Выведете на печать в терминал ее содержимое,
как и всех подкаталогов при помощи функции print_docs(directory)
'''

def print_docs(directory):
    import os
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            print("Каталог:", os.path.join(dirpath, dirname))
        for filename in filenames:
            print("Файл:", os.path.join(dirpath, filename))

print_docs('D:\\git')
