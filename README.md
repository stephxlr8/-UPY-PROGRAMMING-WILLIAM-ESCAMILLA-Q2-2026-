This is gonna blow up everything 

me piro vampiro 

<img width="822" height="655" alt="image" src="https://github.com/user-attachments/assets/2360109a-28d4-4716-bcd3-5feeab64c075" />

 
## CW07 - Git/Github repo

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
  ```
---
# CW09 - Spanish Verb Conjugator

Se agrego la carpeta `Classwork-09-Spanish-Verb-Conjugator` con el programa `Spanish_verb_conjugator.py`, el pseudocodigo `PPP.txt` y el diagrama de flujo correspondiente, que conjuga verbos regulares en español en tiempo presente.

El programa pide un verbo regular en español y lo conjuga para todos los pronombres:

1. Lee el verbo ingresado por el usuario.
2. Separa la raiz de la terminacion (`-ar`, `-er`, `-ir`).
3. Aplica las terminaciones correspondientes segun el tipo de verbo.
4. Imprime la conjugacion completa.

Archivos incluidos:

1. `Spanish_verb_conjugator.py`
   Programa funcional en Python que realiza la conjugacion.

2. `PPP.txt`
   Contiene el pseudocodigo completo siguiendo las reglas de clase:
   - Ingles simple.
   - Usa `<-` para asignaciones.
   - Usa `#` para comentarios.
   - No contiene sintaxis de Python.

3. `Flowchart`
   Diagrama de flujo que muestra la logica del programa: lectura del verbo,
   separacion de raiz y terminacion, seleccion del tipo de terminacion segun
   `-ar`, `-er` o `-ir`, y el ciclo de impresion para cada pronombre.

Ejemplo de uso:

```text
write a spanish verb: hablar
yo hablo
tu hablas
el habla
nosotros hablamos
vosotros hablais
ellos hablan
```
---
# CW10 - School Management System
Se agrego la carpeta `Classwork-10-School-Management-System` con el programa `classwork10.py`, el pseudocodigo `PPP.txt` y el diagrama de flujo correspondiente, que simula un sistema de gestion escolar con login y tres roles distintos.
El programa pide un usuario y contraseña, valida el acceso y muestra un menu distinto segun el rol:
1. Lee el usuario y la contraseña ingresados.
2. Valida las credenciales contra la lista de usuarios registrados.
3. Identifica el rol del usuario (alumno, maestro o coordinador).
4. Muestra el menu correspondiente a su rol.
5. Ejecuta la accion segun el rol: consultar boleta, calificar alumnos o ver listas generales.
Archivos incluidos:
1. `classwork10.py`
   Programa funcional en Python que implementa el sistema de gestion escolar.
2. `PPP.txt`
   Contiene el pseudocodigo completo siguiendo las reglas de clase:
   - Ingles simple.
   - Usa `<-` para asignaciones.
   - Usa `#` para comentarios.
   - No contiene sintaxis de Python.
3. `Flowchart`
   Diagrama de flujo que muestra la logica del programa: validacion del login,
   seleccion de rol, y los tres caminos posibles (boleta del alumno, captura
   de calificaciones del maestro, y listas generales del coordinador).
Ejemplo de uso:
```text
Usuario: jperez
Contrasena: 1234

Bienvenido, Juan Perez (alumno)

Boleta de Juan Perez
Matematicas: 8.5
Programacion: 9.0
Ingles: 7.5

Materias aprobadas: {'Matematicas', 'Programacion'}
Materias pendientes: {'Ingles'}

```

## Declaración de autoría

El contenido de este repositorio fue desarrollado de forma personal por su autor.
No se utilizó ninguna herramienta de inteligencia artificial para la generación del código, documentación o cualquier otro entregable incluido en este proyecto.

---
