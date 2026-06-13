 This is gonna blow up everything 

me piro vampiro 

<img width="822" height="655" alt="image" src="https://github.com/user-attachments/assets/2360109a-28d4-4716-bcd3-5feeab64c075" />

 
## CW07 - Digito verificador de rol UTFSM

Se agrego la carpeta `CW07` con el programa `digito_verificador.py`, que calcula
el digito verificador de un rol UTFSM.

El programa pide un rol sin guion ni digito verificador y aplica el algoritmo
de modulo 11:

1. Invierte el numero del rol.
2. Multiplica cada digito por la secuencia 2, 3, 4, 5, 6, 7 (repitiendola si se
   acaban los numeros).
3. Suma todos los productos.
4. Calcula el modulo 11 de la suma.
5. Resta ese resultado a 11. El valor final es el digito verificador.
   - Si el resultado es 11, el digito verificador es 0.
   - Si el resultado es 10, el digito verificador es K.

Ejemplo de uso:

```
Ingrese el rol sin guion ni digito verificador: 12345678
El digito verificador es: 5
Rol completo: 12345678-5
```

# CW08 - Numerical Integration

  Se agrego la carpeta `CW08` con el programa `numerical_integration.py`, el pseudocodigo `PPP.txt` y el
  diagrama de flujo `Flowchart.png`.

  El programa calcula aproximaciones de integrales definidas usando metodos numericos.

  Archivos incluidos:

  1. `PPP.txt`
     Contiene el pseudocodigo completo siguiendo las reglas de clase:
     - Ingles simple.
     - Usa `<-` para asignaciones.
     - Usa `#` para comentarios.
     - No contiene sintaxis de Python.

  2. `Flowchart.png`
     Contiene el diagrama de flujo exportado como imagen.
     El diagrama muestra:
     - El flujo de iteracion de cada metodo.
     - La decision entre los tres modos disponibles.

  3. `numerical_integration.py`
     Programa funcional en Python con comentarios de:
     - `# INPUT`
     - `# PROCESS`
     - `# OUTPUT`

  Ejemplo de uso:

  ```text
  Seleccione el metodo de integracion:
  1. Rectangular
  2. Trapezoidal
  3. Simpson

  Ingrese una opcion: 2
  Ingrese el limite inferior: 0
  Ingrese el limite superior: 10
  Ingrese la cantidad de subintervalos: 100

  Resultado aproximado: 333.35


# Declaración de autoría

El contenido de este repositorio fue desarrollado de forma personal por su autor.  
No se utilizó ninguna herramienta de inteligencia artificial para la generación del código, documentación o cualquier otro entregable incluido en este proyecto.
