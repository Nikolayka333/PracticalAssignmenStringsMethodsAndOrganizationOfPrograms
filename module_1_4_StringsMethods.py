#Филимонов Николай Андреевич(с пробелами 27!!! символов)
my_string = input('Введите ваши ФИО: ')
# тут пытался сделать, как учили в прошлом уроке, в итоге что-то близкое получилось ниже
print('Здравстуйте,', my_string , '- у вас:', my_string.count(my_string[0:])) # !!!не получилось вывести верное число символов
print('Здравстуйте,', my_string , '- у вас:', my_string.count(my_string[:0]) , '- 1? символов, верно?')
# выше всегда выводит количество символов на 1 больше, не получилось сделать, чтобы выводило верное значение
print('Здравстуйте,', my_string , '- у вас с пробелами:', int(my_string.count(my_string[:0])) - 1, 'символов') # тут выводит правильное количество символов
#заколхозил как смог,не понимаю как можно сделать правильно, путём правильного указания метода или индексации?
print('Здравстуйте,', my_string , '- у вас с пробелами:', len(my_string) , 'символов') # нашел в интернете ещё один способ подсчёта количества символов
print(len(my_string)) # с этой строки всё выводится по заданию!!!
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[-1])


