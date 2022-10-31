'''
Написать регулярное выражение, которое будет проверять формат времени. (14:00 - True, 25:66 - False)
'''

import re

match = re.fullmatch(r"[0-1][0-9]:[0-5][0-9]|[2][0-3]:[0-5][0-9]|[2][4]:[0][0]", input("What time is it now?\n"))
if match:
    print(True)
else:
    print(False)

