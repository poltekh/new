# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200,600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for i0 in range(1, 12, 2):
    for i1 in range(1, 12, 1):
        sd.line(start_point=sd.get_point(100*i1, 50*i0), end_point=sd.get_point(100*i1, 50*i0 - 50), color=sd.COLOR_RED, width=1)
for i2 in range(12):
    sd.line(start_point=sd.get_point(0, 50*i2), end_point=sd.get_point(1200, 50*i2), color=sd.COLOR_RED, width=1)
for i3 in range(2, 13, 2):
    for i4 in range(12):
        sd.line(start_point=sd.get_point(50 + 100*i4, 50*i3), end_point=sd.get_point(50 + 100*i4, 50*i3 - 50), color=sd.COLOR_RED, width=1)
sd.pause()
