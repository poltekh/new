# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
try:
    month = int(user_input)
except ValueError as e:
    print("Ошибка: нужно ввести число")
    exit (1)
print('Вы ввели', month)
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Количество дней: ", 31)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("Количество дней: ", 30)
elif month == 2:
    print("Количество дней: ", 28)
else:
    print("Месяца с таким номером не существует, введите ещё раз")
exit(2)
