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
