"""S2TP1_VectoresPropios.ipynb - SOLUCIONES
# **Ejercicio N°6:** PCA

***Matemáticas para Machine Learning.***

Semana 2 - Lección 1
"""

# LIBRERIAS ================================================
from sympy import *
import numpy as np
import pandas as pd
import math

def sol_potencia_matriz(A:list,n:int):
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

def sol_exponencial_matriz(A:list,t:float):
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

def sol_evolucion_sistema(A:list,tlim:int,x0:list):
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
            expm = Matrix(sol_exponencial_matriz(A,i))
            x_nuevo = x0*expm
            
            for j in range(len(x0)):
                dict_evolucion[j].append(float(x_nuevo[j]))
        return dict_evolucion