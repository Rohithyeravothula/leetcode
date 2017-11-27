def prefix_to_infix(expr, cur):
    if type(expr) != type([]):
        # The expression is a number or variable.
        str(expr)
    elif len(expr) == 2:
        # This is an operator expression with 1 argument.
        return str(expr[1])
    else:
        # This is an operator expression with 2 or more arguments.
        operator = expr[0]
        left_arg = prefix_to_infix([operator] + expr[1:-1], cur)
        right_arg = prefix_to_infix(expr[-1], cur)
        cur.append(left_arg)
        cur.append(operator)
        cur.append(right_arg)
        # return "({0}{1}{2})".format(left_arg, operator, right_arg)

ans = []
prefix_to_infix(["1", "2", "3", "+", "*"], [])
print(ans)