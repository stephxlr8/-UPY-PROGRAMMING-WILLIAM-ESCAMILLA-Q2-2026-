from PIL import Image

config = {}

try:
    file = open("config.txt", "r")
except FileNotFoundError:
    print("Error: no se encontró el archivo config.txt en esta carpeta.")
    raise SystemExit(1)

for line in file:
    line = line.strip()
    if line == "":
        continue
    try:
        parameter, value = line.split("=")
    except ValueError:
        print(f'Error: config.txt está mal formado, la línea "{line}" no tiene "=".')
        file.close()
        raise SystemExit(1)
    try:
        config[parameter.strip()] = float(value) if "." in value else int(value)
    except ValueError:
        print(f'Error: el valor de "{parameter}" en config.txt no es un número.')
        file.close()
        raise SystemExit(1)
file.close()

print(config)


try:
    with open('mandelbrot.csv', 'r') as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    print("Error: no se encontró el archivo mandelbrot.csv. Corre primero el programa del Classwork 11.")
    raise SystemExit(1)

#quita los encabezados
lineas.pop(0)


#desempaquetas variables
try:
    max_iter = config["max_iter"]
    ancho, alto = config['ancho'], config["alto"]
except KeyError as faltante:
    print(f'Error: falta el parámetro {faltante} en config.txt.')
    raise SystemExit(1)

img = Image.new('L', (ancho, alto))
points_drawn = 0

for linea in lineas:
    try:
        row, column, iterations = linea.strip().split(",")
        iterations = int(iterations)
        row = int(row)
        column = int(column)
    except ValueError:
        print(f'Error: mandelbrot.csv está mal formado en la línea "{linea.strip()}" '
              '(debe tener 3 números: row,column,iterations).')
        raise SystemExit(1)

    if row < 0 or row >= alto or column < 0 or column >= ancho:
        print(f"Error: el punto ({row}, {column}) del csv está fuera del tamaño "
              f"{alto}x{ancho} del config.txt. El csv no es consistente con el config: "
              "corre de nuevo el Classwork 11 después de cambiar config.txt.")
        raise SystemExit(1)

    if iterations == max_iter:
        brightness = 0
    else:
        brightness = int((iterations / max_iter) * 255)

    img.putpixel((column, row), brightness)
    points_drawn += 1

expected_points = ancho * alto
if points_drawn != expected_points:
    print(f"WARNING: mandelbrot.csv has {points_drawn} points, but expected {expected_points}. Regenerate the CSV.")

img.save("mandelbrot.png")
print("DONE")
