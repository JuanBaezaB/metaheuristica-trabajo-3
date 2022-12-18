# Extremal Optimization aplicado al problema de la mochila
El programa presenta una solución estocástica llamada Extremal Optimization para la resolución del problema de la mochila.
Para el correcto funcionamiento de este se deben considerar los siguientes puntos:
## Instalación
Para instalar la aplicación se deben seguir los siguientes pasos:
- Para bajar el programa haga click en el siguiente [link](https://github.com/JuanBaezaB/metaheuristica-trabajo-2.git)
- La aplicación funciona sobre python 3.10.5 o superior
- Instalar la biblioteca ``numpy``, ``pandas``, ``matplotlib`` con los siguientes comandos:
```
pip install numpy
pip install pandas
pip install matplotlib
```
## Ejecución
- Para ejecutar se debe ejecutar el comando 
```
python.exe .\ExtremalOptimization.py seed archivo_entrada num_ite tau endtau
```
- Donde:
  - **seed** es un valor entero positivo que indica cuantas semillas probar desde 1 hasta seed
  - **archivo_entrada** es el path al archivo .csv cuya primera fila es el nombre del archivo, las siguientes tres corresponden a la cantidad de objetos (n), capacidad maxima y mejor valor esperado. Las siguientes n líneas representan a los objetos con su id, valor, peso y 1 si fue usado o 0 en caso contrario, separados por comas.
  - **num_ite** es un número entero igual o mayor que 1 para definir el número de iteraciones por ciclo
  - **tau** es el único valor para EO que define el valor de probabilidades
  - **endtau** Es el valor final de tau, que debe ser mayor al tau definido anteriormente. Los calculos se realizarán desde tau, sumando 0.1 por iteracion hasta llegar a ebdtau
- Un ejemplo de entrada es la siguiente:
```
 py.exe .\ExtremalOptimization.py 50 .\Dataset\hardinstances_pisinger\knapPI_11_20_1000.csv 100 1.4 1.9
```

## Salida
La salida representa un diagrama de caja y bigotes de tau hasta endtau en el eje x versus los mejores valores encontrados por cada semilla en el eje Y.

Este programa fue desarrollado en [Github](https://github.com/JuanBaezaB/metaheuristica-trabajo-3)
## Autores
- Juan Baeza Baeza / jbaeza@ing.ucsc.cl / [JuanBaezaB](https://github.com/JuanBaezaB)
- Fernando Cabezas Herrera / fcabezas@ing.ucsc.cl / [FernandoProg](https://github.com/FernandoProg)
