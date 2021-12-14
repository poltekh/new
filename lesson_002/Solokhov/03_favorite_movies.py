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
movies = []
movie = ''
for char in my_favorite_movies:
    if char == ',':
        movies.append(movie)
        movie = ''
    else:
        movie = movie + char
movies.append(movie)
print(movies[0], movies[4], movies[1], movies[3])
