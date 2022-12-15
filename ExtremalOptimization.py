import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

if len(sys.argv) == 6:  # py.exe .\ExtremalOptimization.py 50 .\Dataset\hardinstances_pisinger\knapPI_11_20_1000.csv 100 1.4 1.9
    seed = int(sys.argv[1])
    archivo_entrada = str(sys.argv[2])
    num_ite = int(sys.argv[3])
    tau = float(sys.argv[4])
    endtau = float(sys.argv[5])
    print("semilla: ", seed)
    print("archivo de entrada: ", archivo_entrada)
    print("numero de iteraciones: ", num_ite)
    print("Tau (τ): ", tau)
    print("Tau (τ) de termino: ", endtau)
else:
    print('Error en la entrada de los parametros')
    print('Los paramentros a ingresar son: semila, archivo de entrada, numero de interaciones y Tau (τ)')
    sys.exit(0)

ite = num_ite
num_tau = tau
tauList = []
while tau < endtau:
    list = []
    count = 0
    while count < seed:
        np.random.seed(count)
        num_ite =  ite 
        ncz = np.genfromtxt(archivo_entrada, delimiter=' ', skip_header = 1 , usecols=(1) , skip_footer=2596, dtype = int)            # primer n=nodos c=capacidad z=mejor_solucion en el archivo
        knapback = np.genfromtxt(archivo_entrada, delimiter=',', skip_header = 5 , usecols=(1, 2, 3) , skip_footer=2575, dtype = int) # valor, peso, asignacion
        initial_solution = np.random.randint(2, size=int(ncz[0]))
        while True: # Solucion inicial factible, mejorable para capacidades pequeñas
            if not factibility():
                initial_solution[np.random.randint(int(ncz[0]), size=1)] = 0
            else:
                break

        probabilities = (np.arange(int(ncz[0])) + 1)**-tau 
        fitness = create_fitness()
        fitness_ordenado = np.sort(fitness)

        while 0 < num_ite  and np.sum(initial_solution*knapback[:, 0]) <ncz[2]:
            elegido =  np.random.choice(fitness_ordenado, 1, p=probabilities/np.sum(probabilities)) # AUN SIN USAR, elegir por metodo de la ruleta
            valor_indice = np.where(fitness == elegido)
            valor_indice_random = np.random.choice(valor_indice[0],1)
            if(initial_solution[valor_indice_random]==0):
                initial_solution[valor_indice_random]=1
                if np.sum(initial_solution*knapback[:,1])>ncz[1]:
                    initial_solution[valor_indice_random]=0
            else:
                initial_solution[valor_indice_random]=0
                if np.sum(initial_solution*knapback[:,1])>ncz[1]:
                    initial_solution[valor_indice_random]=1
            num_ite -= 1

        list.append(np.sum(initial_solution*knapback[:,0]))
        count+=1
    tauList.append(list)
    tau += 0.1

plt.suptitle('Diagrama de caja y bigotes', fontsize=14, fontweight='bold')
plt.xlabel('Valor de Tau')
plt.boxplot(tauList)
plt.xticks(np.arange(1, len(tauList) + 1), np.arange(num_tau, tau-0.1, 0.1, dtype=float).round(1))
plt.show()
end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')