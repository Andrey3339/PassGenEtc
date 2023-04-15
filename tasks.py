# Задача 0. Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной.

def task1():
    from random import randint
    n = int(input('Введите длинну списка: '))
    numbers = [randint(0, 10) for _ in range(n)] # генератор списка
    sum = 0
    for el in numbers:
        sum += el
    if sum % 2 == 0:
        print(f'сумма {sum} четная.')
    else:
        print(f'сумма {sum} нечетная.')
    
    print(numbers)

#task1()

# Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня. 
# Определите в какой период выпало больше осадков: в первой или второй половине июня.
# список заполняется случайными от 0 до 25

def task1():
    from random import randint
    num = [randint(0, 25) for _ in range(30)] 
    count1 = count2 = 0
    print(num)
    for el in range(int(len(num) / 2)):
        count1 += num[el]
        count2 += num[el + 15]
    # можно через срезы сделать
    # count1 = sum(num[:int(len(sum) / 2)])
    # count2 = sum(num[int(len(sum) / 2):])
    if count1 > count2:
        print(f'в первую половину выпало больше осадков {count1} > {count2}')
    elif count1 < count2:
        print(f'во вторую половину выпало больше осадков {count1} < {count2}')
    else:
        print(f'в первую и во вторую половину выпало одинаковое количество осадков {count1} = {count2}')

# task1()

# Задача 2. Напишите программу, которая позволит пользователю заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета.

def task2():
    #anketa = {}
    #anketa["имя"] = input('введите имя:  ')
    #anketa["возраст"] = input('введите возраст:  ')
    #anketa["хобби"] = input('введите хобби:  ')
    #anketa["любимое животное"] = input('введите любимое животное:  ')
    # можно так
    anketa = dict(имя = input('введите имя:  '),
                  возраст = int(input('введите возраст:  ')),
                  хобби = input('введите хобби:  '),
                  любимое_животное = input('введите любимое животное:  '))
    #print(anketa)
    # такой вывод интереснее
    for key, value in anketa.items():
        print(f'{key}: {value}')

# task2()

# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел

def task3():
    import random
    lenpswd = int(input('введите длинну пароля:  '))
    substr1 = 'abcdefghijklmnopqrstuvwxyz'
    substr2 = '0123456789'
    substr3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    substr4 = "#$%&'()*+,-./:;<=>?@[\]^_{|}~"
    str = list(substr1 + substr2 + substr3 + substr4)
    for _ in range(10000):
        random.shuffle(str)
    #print("".join(str))    
    #for _ in range(10000):
    #    random.shuffle(str)    
    pswd = [str[random.randint(0, len(str) - 1)] for _ in range(lenpswd)]
    print("".join(pswd))

#def task3_1():
#    length = int(input('введите длинну пароля:  '))
#    letters_and_digits = string.ascii_letters + string.digits
#    password = ''.join(random.sample(letters_and_digits, length))
#    print(password)

task3()
#task3_1()

# Задача 4. Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля. Кассир последовательно вводит в программу
# позиции из чека «ручка», «карандаш», «ластик». Ввод заканчивается, когда введено слово «стоп». Определите сумму чека.

def task4():
    str = input('введите позицию из чека:  ')
    d = { "ручка": 5, "карандаш" : 3, "ластик" : 4 }
    sum = 0
    while str != 'стоп':
        if str in d.keys():
            sum += d[str]
        else: 
            print('такого товара нет')
        str = input('введите позицию из чека:  ')
    print(f'сумма чека:  {sum}')

# task4()

# data = open('test.txt', encoding='utf-8')
# text = data.readlines()
# data.close()

# phrase = text[0].split(':')

# bot = {}
# bot[phrase[0]] = phrase[1]
# print(bot)

# решение задачи
# dictio = [i for i in range(N) if (i%2==0)]



