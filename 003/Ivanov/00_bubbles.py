# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint
sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
for i in range( 800, 816, 5 ):
    sd.circle( sd.Point( i, 300 ))
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for i in range( 300, 501, 20 ):
    sd.circle( sd.Point( i, 300), 10)
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for i in range( 350, 551, 100 ):
    for j in range( 100, 301, 20 ):
        sd.circle( sd.Point( j, i ), 10 )
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for i in range( 100 ):
    x = randint( 20, 550 )
    y = randint( 20 , 1050 )
    r,g,b = randint( 0,255 ), randint( 0,255 ), randint(0, 255)
    sd.circle( sd.Point( y, x ), 10, color = ( r , g , b ) )
sd.pause()

