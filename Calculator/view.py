def get_type():
    type = int(input("Введите тип. 0 - комплексные, 1 - целые числа"))
    return type

def get_value_int():
    a = int(input("Введи число: "))
    b = int(input("Введи число: "))
    return a,b

def get_value_complex():
    a = complex(input("Введи число: "))
    b = complex(input("Введи число: "))
    return a,b

def get_sign(type):
    if type:
        sign = input()
        if sign in ["+","-","/","%","*","//"]:
            return sign
        else:
            print("Ошибка ввода!")
    else:
        sign = input()
        if sign in ["+", "-", "/","*"]:
            return sign
        else:
            print("Ошибка ввода!")