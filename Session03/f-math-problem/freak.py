# from random import *

# x = randint(0,10)
# y = randint(0,10)

# cal = choice("+,-,*,/")

# if cal == "+":
#     result = x + y
# elif cal == "-":
#     result = x - y
# elif cal == "*":
#     result = x * y
# else:
#     result = x / y

# error = randint(-1,0,1)

# print("{0} {1} {2} = {3}".format(x, cal, y, result+error))

from random import radint, choice
# from eval import calc
import eval

x = randint(1, 10)
y = randint(1, 10)
ops = ["+", "-", "*", "/"]

op = choice(ops)

res = calc (x, y, op)

# res = -9999

# if cal == "+":
#     result = x + y
# elif cal == "-":
#     result = x - y
# elif cal == "*":
#     result = x * y
# else:
#     result = x / y

err = choice([-1, 0, 1])
display_res = res + err

print("*" * 20)
print("{0} {1} {2} = {3}".format(x, op, y, display_res))
