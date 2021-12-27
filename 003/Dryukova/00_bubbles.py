# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)



# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

#point=sd.get_point(100, 100)
#radius=50
#for _ in range (3):
#    sd.circle(center_position=point, radius= radius, width=2)
#    radius+=5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

#def bubble (point, step):
#    radius = 50
#    for _ in range(3):
#        sd.circle(center_position=point, radius=radius, width=2)
#        radius += step


# Нарисовать 10 пузырьков в ряд

#for x in range (100, 1100, 100):
#    point=sd.get_point(x, 500)
#    bubble(point=point, step=5)


# Нарисовать три ряда по 10 пузырьков

#for y in range (150, 451, 150):
#    for x in range(100, 1100, 100):
#        point = sd.get_point(x, y)
#        bubble(point=point, step=5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

def bubble (point, step, color):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, color= color, radius=radius, width=2)
        radius += step
for _ in range (100):
    color = sd.random_color()
    point=sd.random_point()
    step=random.randint(2, 10)
    bubble(point=point, color=color, step=step)




sd.pause()


