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


En Tabla se vera asi: 

| Intentos con FOR en segundos |         |         |         |         | Promedio FOR | Speedup = T1/Tdif | Eficiencia=Speedup/NumeroDeHilos | Intentos con NUMPY  en segundos |         |         |         |         | Promedio NUMPY | Speedup = T1/Tdif | Eficiencia=Speedup/NumeroDeHilos |
|------------------------------|---------|---------|---------|---------|--------------|-------------------|----------------------------------|---------------------------------|---------|---------|---------|---------|----------------|-------------------|----------------------------------|
| # de Hilos                   | 1       | 2       | 3       | 4       | 5            |                   |                                  |                                 | 1       | 2       | 3       | 4       | 5              |                   |                                  |         |
| 1                            | 4,05626 | 4,07538 | 4,34959 | 4,16317 | 4,35681      | 4,19605           | 1,00000                          | 1,00000                         | 0,42309 | 0,44774 | 0,59701 | 0,46202 | 0,52259        | 0,47745           | 1,00000                          | 1,00000 |
| 2                            | 2,25593 | 2,02619 | 2,05129 | 1,98994 | 1,96441      | 2,02247           | 2,07471                          | 1,03736                         | 0,41367 | 0,43195 | 0,46815 | 0,48778 | 0,39639        | 0,43792           | 1,09026                          | 0,54513 |
| 4                            | 1,64014 | 1,3672  | 1,29131 | 1,37121 | 1,35329      | 1,36390           | 3,07651                          | 0,76913                         | 0,42255 | 0,64534 | 0,4953  | 0,40163 | 0,48102        | 0,46629           | 1,02393                          | 0,25598 |
| 8                            | 1,21114 | 1,24364 | 1,07963 | 1,1758  | 1,2149       | 1,20061           | 3,49492                          | 0,43686                         | 0,61654 | 0,47188 | 0,50095 | 0,4992  | 0,46537        | 0,49068           | 0,97304                          | 0,12163 |

