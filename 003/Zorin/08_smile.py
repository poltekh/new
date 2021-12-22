# -*- coding: utf-8 -*-

# (определение функций)

import simple_draw as sd
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
sd.resolution = (1200,600)


def smile(x, y, color):
    sd.circle(sd.Point (x,y), 30, color, 1)
    sd.line(sd.Point(x - 10, y + 15), sd.Point(x - 10, y - 5),color, 1)
    sd.line(sd.Point(x + 10, y + 15), sd.Point(x + 10, y - 5),color,1)
    sd.line(sd.Point(x - 15, y - 15), sd.Point(x + 15, y - 15), color, 1)


for i in range(10):
    x = sd.randint(30, 1100)
    y = sd.randint(30, 570)
    color = sd.random_color()
    smile(x , y , color)
sd.pause()
