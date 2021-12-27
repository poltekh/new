# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

spoint=sd.get_point(50, 50)
epoint=sd.get_point(350, 450)
for i in range (7):
    line = sd.line(spoint, epoint, rainbow_colors[i], 5)
    spoint=sd.get_point(50+10*i, 50+10*i)
    epoint=sd.get_point(350+10*i, 450+10*i)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


sd.pause()
