#Intregral of a function
#INPUT

import math


a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Write the method to use (LRM, RRM, MPM, TM): ")

try:
    if "pi" in a:
        a = eval(a.replace("pi", str(math.pi)))
    else:
        a = float(a)
except (ValueError, NameError, SyntaxError):
    print("Error: El límite inferior debe ser numérico")
    raise SystemExit(1)

try:
    if "pi" in b:
        b = eval(b.replace("pi", str(math.pi)))
    else:
        b = float(b)
except (ValueError, NameError, SyntaxError):
    print("Error: El límite superior debe ser numérico")
    raise SystemExit(1)

# Reglas de negocio: Python no las detecta solo, se validan con raise
try:
    if a >= b:
        raise ValueError("El límite inferior debe ser menor que el límite superior")
    if method not in ("LRM", "RRM", "MPM", "MRM", "TM"):
        raise ValueError("El método de integración no es válido. Usa LRM, RRM, MPM o TM")
except ValueError as regla:
    print(f"Error: {regla}")
    raise SystemExit(1)

#PROCESS

area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0

if method == "RRM":
    shift = 1
elif method in ("MPM", "MRM"):
    constant = h / 2

try:
    if method == "TM":
        # Trapecio: extremos con peso 1/2, puntos interiores con peso 1
        for i in range(n + 1):
            xi = a + i * h
            height = eval(f_x, {"math": math, "x": xi, "pi": math.pi})
            if i == 0 or i == n:
                area += height * h / 2
            else:
                area += height * h
    else:
        for i in range(0 + shift, n + shift):
            xi = a + i * h + constant
            height = eval(f_x, {"math": math, "x": xi, "pi": math.pi})
            area += height * h
except NameError:
    print("Error: La función debe estar escrita en términos de x")
    raise SystemExit(1)
except (SyntaxError, TypeError):
    print("Error: La función ingresada no es válida")
    raise SystemExit(1)
except ZeroDivisionError:
    print("Error: La función no está definida en algún punto del intervalo")
    raise SystemExit(1)

#OUTPUT

print(f"The integration of {f_x} is {area:.3f}")
