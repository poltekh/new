# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (500, 500)
sd.background_color=sd.COLOR_BLACK
sx, sy=0, 0
sh=100
high=50
row_brick_n =10
row_n = 10
sdv_b=50

for current_row in range (row_n):
    if current_row%2==0:
        sdv=50
    else: sdv=0

    for current_brick in range (row_brick_n):
        lnx=sx+sdv+sh*current_brick
        lny=sy+high*current_row
        lpoint=sd.get_point(lnx, lny)
        pvx=lnx+sh
        pvy=lny+high
        ppoint=sd.get_point(pvx, pvy)
        sd.rectangle(lpoint, ppoint, sd.random_color(), 3)

sd.pause()
