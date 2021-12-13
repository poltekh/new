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

first_film = my_favorite_movies[0:10]
print(len(my_favorite_movies))
second_film = my_favorite_movies[42:57]
third_film = my_favorite_movies[12:25]
fourth_film = my_favorite_movies[35:40]
print(first_film)
print(second_film)
print(third_film)
print(fourth_film)
