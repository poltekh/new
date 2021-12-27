# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

sd.resolution = (700, 700)


def smalic(x, y, color):
    start_point = sd.get_point(x, y)
    sd.circle(start_point, 50, width=7)
    sd.line(sd.get_point(x - 20, y - 5), sd.get_point(x - 10, y - 20), 2)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), 2)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 20, y - 5), 2)
    sd.line(sd.get_point(x - 15, y + 20), sd.get_point(x - 15, y + 5), 2)
    sd.line(sd.get_point(x + 15, y + 20), sd.get_point(x + 15, y + 5), 2)


for i in range(10):
    point = sd.random_point()
    x = point.x
    y = point.y
    color = sd.random_color()
    smalic(x, y, color)

sd.pause()
