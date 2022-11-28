import numpy as np
import pandas as pd
import time
import sys

start = time.time() 

if len(sys.argv) == 5:
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

end = time.time()
print('Tiempo de ejecución:', end - start,'segundos')