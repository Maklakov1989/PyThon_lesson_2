print(('*' * 25), 'Задание №1 к лекции № 4 НЕ ГОТОВО!!!!', ('*' * 25))
print(('*' * 25), 'Задание №2 к лекции № 4 НЕ ГОТОВО!!!!', ('*' * 25))
# numbers = input('Введите список числел, разделённых пробелом: ')
# numbers = numbers.split(' ')
# numbers = list(numbers)
# my_list = []
# for i in numbers:
#     i = int(i)
#     my_list.append(i)
# print(f"Исходный список: {my_list}")
# new_list = []
# el = 1
# for el in range(0, len(my_list), 2):
#     y = max(my_list[el], my_list[el+1])
#     new_list.append(y)
# print(f'Новый список с элементами больше предудущего: {new_list}')
print(('*' * 25), 'Задание №3 к лекции № 4', ('*' * 25))
my_list = range(20,240)
new_list = [el for el in my_list if el % 21 == 0 or el % 20 == 0]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
