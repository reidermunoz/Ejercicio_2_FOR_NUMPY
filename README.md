# Ejercicio_2_FOR_NUMPY
Tarea de paralelas y distribuidas - Evaluación del speedup y la eficiencia

-Nombre: Reider Andres Muñoz Herrera

-email: reider.munoz@correounivalle.edu.co

-Codigo: 2229712

El programa suma dos vectores de 10 millones de elementos de dos maneras:

una versión con for: suma elemento a elemento usando un ciclo `for`.

una versión con NumPy: suma vectorizada usando A + B.

Y en ambos casos divide el trabajo entre varios procesos (NUM_HILOS = 1, 2, 4, 8) para comparar tiempos, para utilizar el codigo olamente debe cambiar la variable NUM_HILOS y correrlo, la version for y la version Numpy esta en el mismo codigo.

Ejemplo:

NUM_HILOS = 1

NUM_HILOS = 2

NUM_HILOS = 4

NUM_HILOS = 8

Para cada número de hilos se realizaron 5 ejecuciones.
El promedio reportado corresponde al promedio de los 3 valores centrales, descartando el mayor y el menor, con el fin de reducir el efecto de valores atípicos.

## Promedios FOR

1 hilo: 4,19605 s

2 hilos: 2,02247 s

4 hilos: 1,36390 s

8 hilos: 1,20061 s

## Speedup FOR

Fórmula:
Speedup= Tiempo de 1 hilo/ Tiempo de # de hilos

1 hilo: 1,00000

2 hilos: 2,07471

4 hilos: 3,07651

8 hilos: 3,49492


## Eficiencia FOR

Fórmula:
Eficiencia =Speedup/Numero de Hilos

1 hilo: 1,00000

2 hilos: 1,03736

4 hilos: 0,76913

8 hilos: 0,4368


## Promedios NUMPY

1 hilo: 0,47745

2 hilos: 0,43792

4 hilos: 0,46629

8 hilos: 0,49068

## Speedup NUMPY

1 hilo: 1,00000

2 hilos: 1,09026

4 hilos: 1,02393

8 hilos: 0,97304

## Eficiencia NUMPY

1 hilo: 1,00000

2 hilos: 0,54513

4 hilos: 0,25598

8 hilos: 0,12163

