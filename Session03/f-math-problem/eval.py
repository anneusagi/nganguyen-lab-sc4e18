from random import choice

# function arguments / parameters ( tham số đầu vào)
def calc(x, y, op):
    res = 0

    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
    else:
        res = x / y

    return res


print("Hello world")

result = calc(9, 3, "/")
print(result)