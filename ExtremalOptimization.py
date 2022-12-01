import numpy as np
import pandas as pd
import time
import sys

def factibility():
    if np.sum(initial_solution*knapback[:, 1]) <= ncz[1]:
        return True
    else:
        return False

def create_fitness():
    fitness = knapback[:, 0]/knapback[:, 1]
    return fitness

start = time.time() 

if len(sys.argv) == 5:  # py.exe .\ExtremalOptimization.py 1 .\Dataset\hardinstances_pisinger\knapPI_11_20_1000.csv 100 1.4
    seed = int(sys.argv[1])
    archivo_entrada = str(sys.argv[2])
    num_ite = int(sys.argv[3])
    tau = float(sys.argv[4])
    print("semilla: ", seed)
    print("archivo de entrada: ", archivo_entrada)
    print("numero de iteraciones: ", num_ite)
    print("Tau (τ): ", tau)
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: semila, archivo de entrada, numero de interaciones y Tau (τ)')
    sys.exit(0)
    
np.random.seed(seed)

ncz = np.genfromtxt(archivo_entrada, delimiter=' ', skip_header = 1 , usecols=(1) , skip_footer=2596, dtype = int)            # primer n=nodos c=capacidad z=mejor_solucion en el archivo
knapback = np.genfromtxt(archivo_entrada, delimiter=',', skip_header = 5 , usecols=(1, 2, 3) , skip_footer=2575, dtype = int) # valor, peso, asignacion
while True: # Solucion inicial factible, mejorable para capacidades pequeñas
    initial_solution = np.random.randint(2, size=int(ncz[0]))
    if factibility():
        break
probabilities = (np.arange(int(ncz[0])) + 1)**-tau
# np.random.choice(np.arange(int(ncz[0])), 1, p=probabilities/np.sum(probabilities)) # AUN SIN USAR, elegir por metodo de la ruleta
fitness = create_fitness()

end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')