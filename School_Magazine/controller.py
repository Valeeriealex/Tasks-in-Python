import view

main_dct = {}    #список, где имя и фамилия студента - первый ключ,vвнутри которого второй ключ - предмет, содержащий оценки
student_name = []
lesson = []

def start():
    while True:
        op = view.get_op()
        if op == 1:
            student = view.input_student()
            if student not in student_name:
                main_dct [student] = {}
                student_name.append(student)
                if lesson:
                    for less in lesson:
                        main_dct[student][less] = []
        elif op == 2:
            less = view.input_less()
            lesson.append(less)
            for name in student_name:
                main_dct [name] [less] = []
        elif op == 3:
            name, less, mark = view.input_mark()
            main_dct[name][less].append(mark)
        elif op == 4:
            print(main_dct)
        elif op == 5:
            print(f"Оценки {name} - {main_dct[name]}")
        elif op == 6:
            break
        print(main_dct)
