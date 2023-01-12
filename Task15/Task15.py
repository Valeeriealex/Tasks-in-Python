#Задайте число. 
#Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#функция чисел Фибоначчи
def Fibonacci(n): 
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

#функция отрицательных чисел Фибоначчи
def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n): #для индекса в диапазоне от 2 до n
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Введите число для создания списка Фибоначчи: '))
for e in range(1, userNumber + 1): #для переменной в диапозоне от 1 до введенного пользователем числа плюс 1
    list.append(Fibonacci(e)) #добавить в список переменную и первую функцию
    list.insert(0, NegaFibonacci(e)) #добавить в список пернменную и вторую функцию
print(list)