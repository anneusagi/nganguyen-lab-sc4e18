x = int(input("x: "))
cal = input("Operation(+,-,*,/): ")
y = int(input("y: "))

# if cal == '+':
#     print("{0} {1} {2} = {3}".format(x, cal, y, x+y ))


result = 0

if cal == "+":
    result = x + y
elif cal == "-":
    result = x - y
elif cal == "*":
    result = x * y
else:
    result = x / y

print