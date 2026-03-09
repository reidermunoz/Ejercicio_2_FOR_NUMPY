import numpy as np
import time
from multiprocessing import Pool

N = 10_000_000
NUM_HILOS = 8

def suma_for(datos):
    A, B = datos
    C = np.zeros(len(A))
    for i in range(len(A)):
        C[i] = A[i] + B[i]
    return C

def suma_numpy(datos):
    A, B = datos
    return A + B

if __name__ == "__main__":
    A = np.random.randint(0, 10, N)
    B = np.random.randint(0, 10, N)

    partes_A = np.array_split(A, NUM_HILOS)
    partes_B = np.array_split(B, NUM_HILOS)
    datos_partidos = list(zip(partes_A, partes_B))

    # -------- FOR TRADICIONAL --------
    inicio_for = time.time()
    with Pool(processes=NUM_HILOS) as pool:
        resultados_for = pool.map(suma_for, datos_partidos)
    C_for = np.concatenate(resultados_for)
    fin_for = time.time()
    
    print(f"For con {NUM_HILOS} hilos: {fin_for - inicio_for:.5f} segundos")

    # -------- NUMPY VECTORIZADO --------
    inicio_numpy = time.time()
    with Pool(processes=NUM_HILOS) as pool:
        resultados_numpy = pool.map(suma_numpy, datos_partidos)
    C_numpy = np.concatenate(resultados_numpy)
    fin_numpy = time.time()


    print(f"Numpy con {NUM_HILOS} hilos: {fin_numpy - inicio_numpy:.5f} segundos")
    print("Resultados iguales?", np.array_equal(C_for, C_numpy))
   
