# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1300, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

#point = sd.get_point(500,500)
#sd.circle(center_position=point)
#radius = 50
#for i in range (3):
#    sd.circle(center_position=point,radius= radius, width =2)
#    radius += 5

# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг

#def bubble(point, delt):
#    radius = 30
#    for i in range (3):
#        sd.circle(center_position = point, radius = radius, width = 1)
#        radius += delt
#point = sd.get_point(500,500)
#delt = 5
#bubble (point = point, delt = delt)

# Нарисовать 10 пузырьков в ряд

#delt = 0
#for i in range (0, 10, 1):
#    radius = 50
#    point = sd.get_point(100 + delt, 500)
#    for a in range (3):
#        sd.circle(center_position = point, radius = radius, width=1)
#        radius += 5
#    delt = delt + 120

# Нарисовать три ряда по 10 пузырьков

#for i in range (0, 300, 100):
#    delt = 0
#    for a in range (0, 10, 1):
#        radius = 20
#        point = sd.get_point(100 + delt, 100 + i)
#        for b in range (3):
#            sd.circle(center_position = point, radius = radius, width = 1)
#            radius += 5
#        delt += 100

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


#for i in range (100):
#    radius = 30
#    point = sd.random_point()
#    color = sd.random_color()
#    for a in range (3):
#        sd.circle(center_position=point, radius=radius, color = color, width=1)
#        radius += 5

sd.pause()
