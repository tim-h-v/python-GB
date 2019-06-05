import random
from collections import Counter
n = 0
while n == 0:
    try:
        n = int(input('Введите число попыток: '))
    except ValueError:
        pass
ask = [input('Введите имена, нажимая \'Enter\',\nдля выхода \'Стоп\' и \'Enter\'!\n').capitalize()]
if 1 != ask.count('Стоп'):
    while ask.count('Стоп') != 1:
        ask.append(input('Введите имена, нажимая \'Enter\',\nдля выхода \'Стоп\' и \'Enter\'!\n').capitalize())
    ask.remove('Стоп')
    for x in range(1, n - len(ask) + 1):
        random_ask = random.choice(ask)
        ask.append(random_ask)
    list_name = Counter(ask).most_common()
    print('Победило имя - ', list_name[0])
    print(list_name)
input('Нажмите \'Enter\' для выхода')
