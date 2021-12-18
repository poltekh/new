# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
sd.resolution = (720, 525)
for i in range(8):
    for j in range( 10 ):
        sx = 10+100*i
        sy = 10+50*j
        ex = 110+100*i
        ey = 60+50*j
        if j%2!=0:
            sxx = sx-50
            exx = ex-50
        else:
            sxx = sx
            exx = ex
        sd.rectangle( sd.Point(sxx,sy), sd.Point( exx, ey), color = ( 160, 54, 35 ), width = 4 )

sd.pause()
