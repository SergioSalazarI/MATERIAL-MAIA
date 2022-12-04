"""S2TP1_VectoresPropios.ipynb

***Matemáticas para Machine Learning.***

Semana 2 - Lección 1
"""

# Librerias
from sympy import *
import numpy as np
import pandas as pd
import math
import random


class Utils:

    def generador_matrices(self,dim = [2,2], n=3):
        """
        Genera matrices diagonalizables y los parámetros para las funciones calificadoras
        ___________________________________
        Entrada:    Entrada:
        A: [list] Lista que contiene las dimensiones de las matrices. dim[0]=dim[1]
        n: [int] Número de matrices a generar
        ___________________________________
        Salida:
        dataset: [dic] Diccionario con los parámetros de las funciones calificadoras.
        """
        dataset = {"test":[],"power":[],"time":[]}
        i = 0
        while i <n:
            # Matriz diagonal
            A_diag = np.diag(np.random.randint(low=-10,high=10, size=dim[0]))

            # Matriz de cambio de base
            P = np.array(np.random.randint(low=1,high=10,size=(dim[0],dim[1])))

            # Potencia a utilizar para probar la función *calificar_potencia_matriz*
            power = random.randint(2, 10)

            # 'tiempo' a utilizar para probar la función *calificar_pexponencial_matriz*
            t = random.randint(2, 6)

            # Si P es no singular, calcular D. Si el determinante de P es igual a cero, se itera de nuevo
            if(np.linalg.det(P)!=0):
                # Matriz inversa de P, P_inv
                P_inv = np.linalg.inv(P)

                # Matriz A
                A = P_inv*A_diag*P

                # Redondear las entradas de A
                A = A.round(0)

                # Agregar los parámetros a dataset
                dataset["test"].append(A.tolist())
                dataset["power"].append(power)
                dataset["time"].append(t)

                # Actualizar el paso
                i += 1
        return dataset

    def sol_potencia_matriz(self,A:list,n:int):
        """
        Calcula la exponencial de la matriz A
        ___________________________________
        Entrada:    Entrada:
        A: [list] Lista que contiene las filas de A. A es diagonalizable.
        t: [int] Tiempo en el cual se calcula la función exponencial.
        ___________________________________
        Salida:
        expA: [list] Lista con las filas resultantes de calcular la exponcial de la matriz A.
        """
        # Definir la matriz cuya potencia es deseada
        A_n = Matrix(A)

        # Diagonalizar A_n
        P,D = A_n.diagonalize()

        # Calcular la potencia n-ésima de D
        D_n = D**n
        
        # Calcular la potencia n-ésima de A por medio de la potencia n-ésima de n
        A_n = P*D_n*(P.inv())

        # Transformar de estructura Matriz, a estructura de lista
        A_n = A_n.tolist()

        # Revolver la matriz resultante de la operación potencia
        return A_n

    def calificar_potencia_matriz(self,sol_tentativa,data_test):
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
        sol_correcta = [[self.sol_potencia_matriz(sol_correcta["test"][i],sol_correcta["power"][i])] for i in range(len(sol_correcta))]
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


    def sol_exponencial_matriz(self,A:list,t:float):
        """
        Calcula la exponencial de la matriz A
        ___________________________________
        Entrada:    Entrada:
        A: [list] Lista que contiene las filas de A. A es diagonalizable.
        t: [int] Tiempo en el cual se calcula la función exponencial.
        ___________________________________
        Salida:
        expA: [list] Lista con las filas resultantes de calcular la exponcial de la matriz A.
        """
        # Transformar la lista A en clase Matrix
        A_m = Matrix(A)
        
        # Calcular la matriz no singular P y la matriz diagonal D.
        P, D = A_m.diagonalize()  
        
        # Declarar la variable que almacena la exponencial de la matriz D
        exp_D = D

        # Precisión de las entradas de exp_D
        d_int=3

        for i in range(sqrt(len(D))):
            # Calcular la exponencial por medio de la función math.exp()
            # Redondear con precisión de 3 decimales
            try:
                exp_D[i,i] = round(math.exp(D[i,i]*t),d_int)
            except OverflowError:
                exp_D[i,i] = 100000#float('inf')
        
        # Calcular la exponencial de la matriz original
        expA = P*(exp_D)*P.inv()
        
        # Transforma el dato de la clase Matrix a la estructura list
        expA = expA.tolist()
        return expA

    def calificar_exponencial_matriz(self,sol_tentativa,data_test):
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
        sol_correcta = [[self.sol_exponencial_matriz(sol_correcta["test"][i],sol_correcta["time"][i])] for i in range(len(sol_correcta))]
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

    def sol_evolucion_sistema(self,A:list,tlim:int,x0:list):
        """
        Calcula la evolución del sistema con matriz de estados A y condición inicial x0 desde t=0 hasta tlim.
        ___________________________________
        Entrada:
        A: [list] Matriz de dinámicas del sistema
        x0: [list] Lista que contiene la distribución inicial
        t: [int] Tiempo en el cual se calcula el estado del sistema.
        ___________________________________
        Salida:
        dict_evolucion: [dic] Diccionario que contiene las probabilidades en t, dada la condición inicial x0.
        """
        dict_evolucion = {}
        for i in range(len(x0)):
            dict_evolucion[i] = [x0[i]]
        
        x0 = Matrix(x0).T
        for i in range(tlim):
            expm = Matrix(self.sol_exponencial_matriz(A,i))
            x_nuevo = x0*expm
            
            for j in range(len(x0)):
                dict_evolucion[j].append(float(x_nuevo[j]))
        return dict_evolucion