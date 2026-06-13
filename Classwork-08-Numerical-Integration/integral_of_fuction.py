#Intregral of a function
#INPUT

import math


a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Write the method to use (RRM, LRM, MRM, T): ")

if "pi" in a:
    a = eval(a.replace("pi", str(math.pi)) )
else:
    a = float(a)

if b == "pi":
    b = math.pi
else:
    b = float(b)

#PROCESS

area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0

if method == "RRM":
    shift = 1
elif method == "MRM":
    constant = h / 2

for i in range (0 + shift, n + shift):
    xi = a + i * h + constant
    height = eval(f_x.replace("x", str(xi)))
    area += height * h

#OUTPUT

print(f"The integration of {f_x} is {area:.2f}")