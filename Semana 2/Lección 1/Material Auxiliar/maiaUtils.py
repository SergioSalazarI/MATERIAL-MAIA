"""S2TP1_VectoresPropios.ipynb

***Matemáticas para Machine Learning.***

Semana 2 - Lección 1
"""

# LIBRERIAS ================================================
# Básicas
import numpy as np
import pandas as pd
from sympy import *

# Auxiliar
from IPython.display import display, HTML
from mtr import manipulate_ipython

# datos
from datos import *

# soluciones
from soluciones import *

def calificar_potencia_matriz(sol_tentativa,data_test):
        """
        Función para calificar *potencia_matriz*
        ___________________________________
        Entrada:
        sol_tentativa: [list] Lista que contiene los resultados de la función *potencia_matriz* del estudiante.
        ___________________________________
        Salida:
        En caso de encontrar algún errror retorna un mensaje indicando la matriz que cuya función *potencia_matriz* es incorrecta.
        """

        # DataFrame de la solución calculada por el estudiante
        sol_tentativa = pd.DataFrame(sol_tentativa)
        
        # DataFrame que almacena la solución correcta
        sol_correcta = pd.DataFrame(data_test)
        sol_correcta = [[sol_potencia_matriz(sol_correcta["test"][i],sol_correcta["power"][i])] for i in range(len(sol_correcta))]
        sol_correcta = pd.DataFrame(sol_correcta)

        # Comparar la solución del estudiante y la solución correcta
        for i in range(len(sol_correcta)):

            # Booleano que indica si la solución tentativa es correcta.
            sol_tentativa_correcta = False

            # soluciones a comparar
            sol_c = sol_correcta.iloc[i,:]
            sol_t = sol_tentativa.iloc[i,:]

            # compara las soluciones i-ésimas
            if (sol_t == sol_c).all():
                sol_tentativa_correcta = True
            
            # Matriz utilizada durante la prueba
            A_test = data_test["test"][i]

            # Si la solución no es correcta, imprime la matriz cuya función *potencia_matriz* es incorrecta
            assert sol_tentativa_correcta, f"Error en la prueba {i}. La función *Potencia de una matriz* no es correcta para A={A_test}"

def calificar_exponencial_matriz(sol_tentativa,data_test):
        """
        Función para calificar *potencia_matriz*
        ___________________________________
        Entrada:
        sol_tentativa: [list] Lista que contiene los resultados de la función *potencia_matriz* del estudiante.
        ___________________________________
        Salida:
        En caso de encontrar algún errror retorna un mensaje indicando la matriz que cuya función *exponencial_matriz* es incorrecta.
        """
        # DataFrame de la solución calculada por el estudiante
        sol_tentativa = pd.DataFrame(sol_tentativa)

        # DataFrame que almacena la solución correcta
        sol_correcta = pd.DataFrame(data_test)
        sol_correcta = [[sol_exponencial_matriz(sol_correcta["test"][i],sol_correcta["time"][i])] for i in range(len(sol_correcta))]
        sol_correcta = pd.DataFrame(sol_correcta)

        # Comparar la solución del estudiante y la solución correcta
        for i in range(len(sol_correcta)):

            # Booleano que indica si la solución tentativa es correcta.
            sol_tentativa_correcta = False

            # soluciones a comparar
            sol_c = sol_correcta.iloc[i,:]
            sol_t = sol_tentativa.iloc[i,:]

            # compara las soluciones i-ésimas
            if (sol_t == sol_c).all():
                sol_tentativa_correcta = True

            # Matriz utilizada durante la prueba
            A_test = data_test["test"][i]

            # Si la solución no es correcta, imprime la matriz cuya función *potencia_matriz* es incorrecta
            assert sol_tentativa_correcta, f"Error en la prueba {i}. La función *exponencial de una matriz* no es correcta para A={A_test}"