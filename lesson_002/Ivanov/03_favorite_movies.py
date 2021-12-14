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

# TODO здесь ваш код
print( my_favorite_movies[0:my_favorite_movies.find(',')])
print( my_favorite_movies[-1:my_favorite_movies.rfind( ','):-1] ) #так прикольнее, но вот правильный вариант: print( my_favorite_movies[my_favorite_movies.rfind(',')+2:-1])
print( my_favorite_movies[my_favorite_movies.find(',')+2:my_favorite_movies.find( ',', 12)])
print( my_favorite_movies[my_favorite_movies.rfind( ',', 1, 40)+2:my_favorite_movies.rfind( ',')])