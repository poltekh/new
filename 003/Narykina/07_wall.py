import simple_draw as sd

sd.resolution = (1000, 500)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# координаты начала стены
START_X = 0
START_Y = 0
# параметры кирпичика(ширина высота)
BRICK_WIDTH = 100
BRICK_HEIGHT = 50

ROW_BRICK_NUMBER = 10 # количество кирпичей в ряду
ROW_NUMBER = 10 # число рядов
BRICK_OFFSET = int(0.5 * BRICK_WIDTH) # смещение

for current_row in range(ROW_NUMBER):
    # вот здесь определяется, сколько именно составит смещение.
    # для четного ряда будет 50, для нечетного - 0
    OFFSET = 50 if current_row % 2 == 0 else 0 
       
    for current_brick in range(ROW_BRICK_NUMBER): # рисуем кирпич
        # добавим смещение к началу отсчета для оси X
        left_bottom_x = START_X + OFFSET + BRICK_WIDTH * current_brick # координата х нижнего левого угла кирпичика
        left_bottom_y = START_Y + BRICK_HEIGHT * current_row # координата y нижнего левого угла кирпичика
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y) # создаем точку в месте, где будет левый нижний угол
        # то же самое для верхней правой
        right_top_x = left_bottom_x + BRICK_WIDTH
        right_top_y = left_bottom_y + BRICK_HEIGHT
        right_top = sd.get_point(right_top_x, right_top_y)
        # рисуем прямоугольник 
        sd.rectangle(left_bottom, right_top, sd.COLOR_RED, width=3)
        #            левая нижняя, правая верняя,цвет, ширина линий