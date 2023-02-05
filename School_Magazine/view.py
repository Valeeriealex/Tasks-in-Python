def get_op():
    op = int(input("1 - добавить студента, 2 - добавить предмет, 3 - добавить оценку,\
    4 - показать список всех студентов, 5 - показать информацию о студенте, 6 - выход"))
    return op

def input_student():
    name = input("Ввесдите Фамилию и Имя: ")
    return name

def input_less():
    less = input("Введите предмет: ")
    return less

def input_mark():
    name = input("Введите имя: ")
    less = input("Введите предмет: ")
    mark = input("Введите оценку: ")
    return name, less, mark

def get_name_to_show():
    name = input("Введите имя для просмотра оценок: ")
    return name


