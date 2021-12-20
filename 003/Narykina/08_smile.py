# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 600)
def draw_smile(x_pos:int,y_pos:int,color:tuple):
	center_pos = sd.Point(x_pos, y_pos) # по-варварски приводим тип центра круга к точке, лучше использовать get_point
	# отступы по осям
	out_y = 10 
	out_x = 15

	sd.circle(center_pos,color=color) # круг по координатам центра и цветом color
	# расчеты координат точек для глаз и улыбки
	eyecoord1 = sd.Point(x_pos+out_x,y_pos+out_y) 
	eyecoord2 = sd.Point(x_pos-out_x,y_pos+out_y)
	smile1 = sd.Point(x_pos-out_x,y_pos-out_y)
	smile2 = sd.Point(x_pos+out_x,y_pos-out_y)
	# отрисовка линий по расчетам
	sd.line(start_point=eyecoord1, end_point=eyecoord1, color=color, width=10)
	sd.line(start_point=eyecoord2, end_point=eyecoord2, color=color, width=10)
	sd.line(start_point=smile1,end_point=smile2,color=color,width=10)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

from random import randint # возьмем генератор случайных целых чисел из библиотеки random
for i in range(10): # для десяти смайликов
# создаем случайную координату в диапозоне
    x = randint(0, 1200)
    y = randint(0, 600)
# выбираем случайные значения для компонентов цветов в каналах красный, зеленый и синий (RGB)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    draw_smile(x,y,(r,g,b)) # собираем все вместе и вызываем функцию
sd.pause()
