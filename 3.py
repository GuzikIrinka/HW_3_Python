# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from traceback import print_list

exit()
myList = [2, 3, 5, 9, 3]
print(myList)
sumOfElements = 0
for i in range (1, len(myList), 2):
    sumOfElements = sumOfElements + myList[i]
print('Сумма элементов списка, стоящих на нечётной позиции:', sumOfElements)



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

someList = [int(input()) for _ in range(int(input()))]

secondList = []

for i in range (len(someList) // 2 + len(someList) % 2):
    secondList.append(someList[i] * someList[len(someList) -1 -i])
print(secondList)