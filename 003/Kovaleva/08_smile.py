# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

sd.resolution = (500, 500)
sd.background_color = sd.COLOR_WHITE


def smile (x, y, color):
    start=sd.get_point(x, y)
    sd.circle(start, 50, color, 3)
    sd.line(sd.get_point(x-25, y-25), sd.get_point(x-5, y-5), color, 5)
    sd.line(sd.get_point(x-5, y-5), sd.get_point(x+5, y-5), color, 5)
    sd.line(sd.get_point(x+5, y-5), sd.get_point(x+25, y-25), color, 5)
    sd.line(sd.get_point(x-15, y-15), sd.get_point(x+15, y-15), color, 4)
    sd.circle(sd.get_point(x-15, y+15), 10, sd.COLOR_BLACK, 3)
    sd.circle(sd.get_point(x+15, y+15), 10, sd.COLOR_BLACK, 3)

for _ in range (10):
    point = sd.random_point()
    x=point.x
    y=point.y
    smile(x, y, sd.random_color())



sd.pause()
