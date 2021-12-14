# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (1000, 500)
start_x = 0
start_y = 0
width = 100
height = 50
row_brick_number = 10
row_number = 10
brick_offset = int(0.5 * width)

for current_row in range(row_number):
    offset = 50 if current_row % 2 == 0 else 0

    for current_brick in range(row_brick_number):
        left_bottom_x = start_x + offset + width * current_brick
        left_bottom_y = start_y + height * current_row
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top_x = left_bottom_x + width
        right_top_y = left_bottom_y + height
        right_top = sd.get_point(right_top_x, right_top_y)
        sd.rectangle(left_bottom, right_top, sd.COLOR_YELLOW, width=3)

sd.pause()
