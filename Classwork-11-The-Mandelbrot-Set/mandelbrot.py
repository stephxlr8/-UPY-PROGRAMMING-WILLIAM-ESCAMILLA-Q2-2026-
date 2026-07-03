# ====================================================
# Classwork #11 - The Mandelbrot Set
# Computes the escape-time (number of iterations before
# |z| > 2) for every point of a grid and saves the
# results to a CSV file.
#
# Rules followed:
#   - config.txt is read once, at the start (no hardcoding)
#   - complex is used for z and c (no manual real/imag split)
#   - one CSV row per grid point: fila,columna,iteraciones
#   - no functions (def) are used
# ====================================================

# ---------------------------------------------------
# INPUT: read the configuration parameters from config.txt
# ---------------------------------------------------
config = {}
archivo = open('config.txt', 'r')
for linea in archivo:
    clave, valor = linea.strip().split('=')
    config[clave] = float(valor)
archivo.close()

# ---------------------------------------------------
# PROCESS: extract and prepare the grid parameters
# ---------------------------------------------------
ancho = int(config['ancho'])
alto = int(config['alto'])
real_min = config['real_min']
real_max = config['real_max']
imag_min = config['imag_min']
imag_max = config['imag_max']
max_iter = int(config['max_iter'])

# ---------------------------------------------------
# OUTPUT: open the CSV file and write the header row
# ---------------------------------------------------
salida = open('mandelbrot.csv', 'w')
salida.write('fila,columna,iteraciones\n')

# ---------------------------------------------------
# PROCESS: sweep every point (pixel) of the grid
# ---------------------------------------------------
for fila in range(alto):
    for columna in range(ancho):

        # PROCESS: map the pixel (fila, columna) to a complex number c
        real = real_min + (columna / ancho) * (real_max - real_min)
        imag = imag_min + (fila / alto) * (imag_max - imag_min)
        c = complex(real, imag)

        # PROCESS: apply z <- z*z + c and count iterations until escape
        z = 0 + 0j
        iteraciones = 0
        while abs(z) <= 2 and iteraciones < max_iter:
            z = z * z + c
            iteraciones += 1

        # OUTPUT: save this point's escape-time result to the CSV file
        salida.write(f'{fila},{columna},{iteraciones}\n')

# ---------------------------------------------------
# OUTPUT: close the CSV file once all points are processed
# ---------------------------------------------------
salida.close()

print('Done. Results saved to mandelbrot.csv')
