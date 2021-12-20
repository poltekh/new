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
<<<<<<< HEAD
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

=======
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
>>>>>>> 12eef8ccb11bebf8d2c24e207d99da6575481a28
