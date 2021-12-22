# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200,600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for i0 in range(1, 11, 2):
    for i1 in range(12):
        sd.line(start_point = (100*i1, 50*i0), end_point= (100*i1 + 100, 50*i0), color = sd.COLOR_RED)

# TODO здесь ваш код

sd.pause()
