
## 🚀 Test Programación Kyocera

## Información

Este repositorio esta creado con el fin de compartir las respustas y desarrollo del test de programación para la postulación de Analista Programador en la empresa Kyocera


 🟢 = Completados
 
 🟠 = Falta por completar

## 🚀 Ejercicios de programación:
Lenguaje de programación: Python

Para probar via web ir al siguiente enlace.

https://stackblitz.com/edit/secret-python-en1gk5?file=main.py


🟠 1. Escriba una función/método que determine la cantidad de 0’s a la derecha de n! (factorial). 

🟢 2. Escriba una función/método tal que dado un número entero, entregue su representación en palabras (Ej. 145,“ciento cuarenta y cinco”). 

🟠 3. Considere un tablero de ajedrez de NxN, realice un algoritmo que visite cada espacio del tablero, usando
solamente los movimientos de un caballo. (Puntos extras si se visita cada espacio una sola vez). 

## 🚀 Ejercicios de Base de Datos
## SQL: 
Los ejercicios de SQL estan realizados en TSQL, para el ejercicio 1 se adjunta dentro de la carpeta.
 
🟢 1. Un colegio necesita un sistema para administrar sus cursos. El sistema tiene que suportar que se le ingresen
varios cursos. Cada curso tendrá un profesor a cargo y una serie de alumnos inscritos. Cada profesor, así como
cada alumno puede estar en más de un curso. Además cada curso tendrá una cantidad no determinada de
pruebas, y el sistema debe permitir ingresar la nota para cada alumno en cada prueba. Todas las pruebas valen
lo mismo.

a. Escriba a continuación las tablas que utilizaría para resolver este problema con los campos y llaves de éstas.
Intente hacer el sistema lo más robusto posible, pero sin incluir datos adicionales a los que se plantean acá.

b. Escriba un Query que entregue la lista de alumnos para el curso “programación.

c. Escriba un Query que calcule el promedio de notas de un alumno en un curso.

d. Escriba un Query que entregue a los alumnos y el promedio que tiene en cada ramo.

e. Escriba un Query que lista a todos los alumnos con más de un ramo con promedio rojo. 

Para resolver este ejercicio se 3 archivos que se pueden encontrar en la carpeta SQL:

1- TestColegioDB: Creacion de la base de datos y sus tablas.

2- Insert_TestColegioDB: Insert correspondiente a cada tabla (10) por cada tabla.

3- Query: Querys solicitadas.

🟢 2. Se tiene una tabla con información de jugadores de tenis:
PLAYERS (Nombre, Pais, Ranking). Suponga que Ranking es un número de 1 a 100 que es distinto para cada
jugador. Si la tabla en un momento dado tiene solo 20 tuplas, indique cuantas tuplas tiene la tabla que resulta
de la siguiente consulta:
SELECT c1.Nombre, c2.Nombre FROM PLAYERS c1, PLAYERS c2 WHERE c1.Ranking > c2.Ranking

a. 400

## b. 190  

c. 20

d. imposible saberlo

La respuesta es b) 190 y el desarrollo se encuentra en el archivo SQL2/Respuesta.txt

