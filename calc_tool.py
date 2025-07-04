def calculator(expr):
    try:
        return eval(expr)
    except:
        return "Invalid math expression."