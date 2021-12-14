# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
for i in range(600,616,5):
	sd.circle(sd.Point(i,300))

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_bubble(start_x: int,start_y: int,color=(255, 255, 0)):
	for i in range(start_x,start_x+16):
		sd.circle(sd.Point(i,start_y,),color=color)

"""# Нарисовать 10 пузырьков в ряд
x = 50
for _ in range(10):
	draw_bubble(x,300)
	x+=50

# Нарисовать три ряда по 10 пузырьков

y = 100
for row in range(3):
        x = 50
        for _ in range(10):
                draw_bubble(x,y)
                x+=50
        y+= 100

"""
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for __ in range(100):
	x = randint(0,1201)
	y = randint(0,600)
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)
	color = (r,g,b)
	draw_bubble(x,y,color)

sd.pause()
