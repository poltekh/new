#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo2 = ['lion', 'bear', 'kangaroo', 'elephant', 'monkey', ]
print(zoo2)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo2 = zoo2 + birds
print(zoo2)

# уберите слона
#  и выведите список на консоль
zoo2.remove('elephant')
print(zoo2)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print(zoo2.index('lion') + 1, zoo2.index('lark') + 1)


