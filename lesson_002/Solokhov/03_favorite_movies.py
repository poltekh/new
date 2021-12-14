#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
arr = []
sl = ""
for i in my_favorite_movies:
    if(i != ","):
        sl = sl + i
    else:
        arr.append(sl)
        sl = ""
arr.append(sl)
print(arr[0], arr[4], arr[1], arr[3])