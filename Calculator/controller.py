import view
import math_op

def start():
    type = view.get_type()
    if type:
        a,b = view.get_value_int()
    else:
        a,b = view.get_value_complex()

    math_op.init(a,b)
    sign = view.get_sign(type)
    res = "Ошибка знака"
    if sign== "+":
        res = math_op.summ()
    elif sign== "-":
        res = math_op.diff()
    elif sign== "*":
        res = math_op.multi()
    elif sign== "/":
        res = math_op.dellen()
    elif sign== "//":
        res = math_op.cel_del()
    elif sign== "%":
        res = math_op.proc_del()

    view.out_res(res)