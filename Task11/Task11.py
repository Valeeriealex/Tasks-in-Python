#Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]

sum = 0
for i in range(1, len(list), 2):
    #if i in list %2 != 0:
        sum += list[i]
print(f"{list} -> сумма элементов на нечётных позициях: {sum}")

# number = int(input('Введите размер списка: '))
# list = []
# sum = 0
# for i in range(number):
#     list_number = int(input(f'Введите число {i+1} '))
#     list.append(list_number)
#     if i % 2 != 0:
#         sum += list[i]
# print(list)
# print(f'Сумма нечетных чисел равна {sum}')