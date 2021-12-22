# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
sd.resolution = (1200,600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, color):
    sd.circle(center_position = (x,y), radius = 30, color = color, width = 1)
    sd.line(start_point = (x - 5,y + 5), end_point = (x - 5,y - 5), color = color, width = 1)
    sd.line(start_point = (x + 5,y + 5), end_point = (x + 5,y - 5), color = color, width = 1)
    sd.line(start_point = (x - 10, y - 10), end_point = (x + 10,y - 10), color = color, width = 1)
for i in range(10):
    x = sd.randint(30, 1100)
    y = sd.randint(30, 570)
    color = sd.random_color()
    smile(x = x, y = y, color = color)
sd.pause()
