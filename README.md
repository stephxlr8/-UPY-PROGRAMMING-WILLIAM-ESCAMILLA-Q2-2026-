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
Classwork #10 — School Management System

Sistema de gestión escolar hecho en Python puro (sin librerías externas) para la materia de Programación, TSU en Ciencia de Datos — UPY.

Descripción

Programa de consola que simula un sistema escolar con login y tres roles distintos: alumno, maestro y coordinador. Cada rol tiene su propio menú y permisos.

Restricción de la consigna: solo se permiten los built-ins input, print, while e if/elif/else. Sin funciones (def) ni librerías externas.

Estructuras usadas

EstructuraUso en el programaDiccionariousuarios (datos de login y rol), calificaciones (notas por alumno y materia)Tuplamaterias (lista fija de materias)Setaprobadas / pendientes (materias aprobadas vs. pendientes del alumno)

Roles y funcionalidad

Alumno


Ve su boleta de calificaciones (Matemáticas, Programación, Inglés).
El programa calcula automáticamente qué materias aprobó (≥ 8.0) y cuáles tiene pendientes.


Maestro


Ve la lista completa de alumnos.
Puede capturar/actualizar la calificación de un alumno en una materia específica.
Puede calificar a varios alumnos en la misma sesión.


Coordinador


Ve la lista de maestros.
Ve la lista de materias.
Ve la lista completa de alumnos con todas sus calificaciones.


Usuarios de prueba

UsuarioContraseñaRoljperez1234alumnoamartin1234alumnocsilva1234alumnolhdez1234alumnodgomez1234alumnofcruz1234alumnomlopez1234maestrorgarcia1234coordinador

Cómo correrlo

bashpython classwork10.py

Al iniciar, te pedirá usuario y contraseña. Usa cualquiera de la tabla de arriba para probar los distintos roles.

Estructura del repo

.
├── classwork10.py     # Código principal
├── PPP.txt             # Pseudocódigo (formato PPP, en inglés)
├── diagrama.mmd        # Diagrama de flujo en Mermaid
└── README.md


## Declaración de autoría

El contenido de este repositorio fue desarrollado de forma personal por su autor.
No se utilizó ninguna herramienta de inteligencia artificial para la generación del código, documentación o cualquier otro entregable incluido en este proyecto.

---
