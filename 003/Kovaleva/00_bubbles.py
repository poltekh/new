# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
#for i in range(600, 616, 5):
#    sd.circle(sd.Point(i, 300))

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color = sd.random_color(), width=2)
point = sd.get_point(500, 500)
bubble (point=point, step=10)

# Нарисовать 10 пузырьков в ряд
#for i in range(6, 1000, 100):
#    sd.circle(sd.Point(i, 300))

# Нарисовать три ряда по 10 пузырьков
for y in range (100, 400 , 100):
    for x in range (100, 1100 , 100):
        point = sd.get_point(x,y)
        bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    point = sd.random_point()
    bubble(point=point,step=5)

sd.pause()

