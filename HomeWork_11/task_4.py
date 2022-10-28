'''
Написать программу, которая должна определить город по почтовому индексу. (Возьмите города РБ, можно только областные).
'''

import re

def sity_index_search(index):
    sity_index = {
        "224000": "Брест",
        "210000": "Витебск",
        "246000": "Гомель",
        "230000": "Гродно",
        "220000": "Минск",
        "212000": "Могилев"
    }
    match = re.fullmatch(r"[2][1-4][0|2|4|6][0]{3}", index)
    if match:
        return sity_index[index]
    else:
        return f"Regional city with index: '{index}' not found."

print(sity_index_search(index=input("Enter index of the regional city of Belarus.\n")))

