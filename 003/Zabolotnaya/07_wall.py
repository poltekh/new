# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
startx=0
starty=0
a=100
b=50
c=10
d=10
startx=0
starty=0
for i in range(d):
    s=50 if i%2==0 else 0
    for k in range(c):
        left_bottom_x=startx+s+a*k
        left_bottom_y = starty + s + b * i
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top_x=left_bottom_x+a
        right_top_y=left_bottom_y+b
        right_top = sd.get_point(right_top_x, right_top_y)
        sd.rectangle(left_bottom, right_top, sd.COLOR_RED, width=3)


