# LIBRERIAS ================================================
import numpy as np
import random

def generador_matrices(dim = [2,2], n=3):
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