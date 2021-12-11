#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
spisok1 = garden_set|meadow_set


print (spisok1)

# выведите на консоль те, которые растут и там и там
spisok2 = garden_set & meadow_set

print (spisok2)

# выведите на консоль те, которые растут в саду, но не растут на лугу
spisok3 = garden_set - meadow_set

print (spisok3)

# выведите на консоль те, которые растут на лугу, но не растут в саду
spisok4 = meadow_set - garden_set

print (spisok4)


