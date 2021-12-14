#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с
# помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
buffer = ""
list_of_fav = []
for char in my_favorite_movies:
    if char == ",":
        list_of_fav.append(buffer)
        buffer = ""
    else:
        buffer += char
list_of_fav.append(buffer)
queue = [0,-1,1,-2]
for i in queue:
    print(list_of_fav[i].strip())
