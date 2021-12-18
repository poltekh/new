# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint
import random
sd.resolution = ( 1200, 700 )
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile( sx, sy, r,g,b):
    sd.circle( sd.Point( sx, sy ), color = ( r,g,b), radius = 60, width = 3)
    sd.ellipse( sd.Point( sx-40, sy-45 ), sd.Point( sx+40, sy+10 ), color = ( r,g,b ), width = 3)
    sd.rectangle( sd.Point( sx-40, sy-23 ), sd.Point( sx+40, sy+23 ), color = ( 0, 8, 98 ), width = 0)
    sd.circle( sd.Point( sx-22, sy+20 ), color = ( 0, 100, 100 ), radius = 15, width = 2)
    sd.circle(sd.Point(sx + 22, sy + 20), color=(0, 100, 100), radius=15, width=2)
    x = randint( 17, 28 )
    y = randint( 17, 28 )
    sd.circle(sd.Point(sx-x, sy + y), color=( 'blue' ), radius=5, width=0)
    sd.circle(sd.Point(sx + x, sy + y), color=( 'blue' ), radius=5, width=0)
    return
s = []
for i in range( 60, 1140, 60 ):
    s.append( i )
q = []
for i in range( 60, 640, 60 ):
    q.append( i )
for i in range( 10 ):
    x = random.choice( s )
    s.remove( x )
    y = random.choice( q )
    q.remove( y )
    r, g, b = randint( 0,255 ), randint( 0,255 ), randint( 0,255 )
    smile( x, y, r, g, b )
sd.pause()
