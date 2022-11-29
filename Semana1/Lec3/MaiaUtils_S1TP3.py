"""S1TP3_SolucionesBasicas.ipynb - UTILS """

# Librerias
import numpy as np
import pandas as pd
import sympy
import sys
from IPython.display import display, HTML
from itertools import combinations


class MaiaUtils:

    def pretty_print(self, df):
        if isinstance(df, dict):
            df = pd.DataFrame(df)
        df['Soluciones'] = df.apply(self.redondear_valores, axis=1)

        return display(HTML(df.to_html().replace("], [", "]<br> [")))

    def _soluciones_basicas_solucion(self, A, b, handle=True):
        """
        Encuentra las soluciones básicas de un sistema de ecuaciones de la forma:
          Ax = b

        Parámetros
        ----------
        A: np.array
          Matriz A (mxn)
        b: np.array
          Vector b (nx1)
        handle: bool
          Si manejar o no las submatrices singulares (reducción del subsistema eliminando la dependencia lineal)

        Retorna
        -------
        out: dict
          Diccionario con todas las soluciones básicas del sistema Ax=b en el formato establecido.

        """
        # Cambio de formato de vectores de entrada
        b = np.array(b).reshape(-1, 1)
        A_or = np.array(A).copy()

        # Transforma a forma canónica e identifica filas con pivote
        Ab = np.c_[A, b]
        _, inds = sympy.Matrix(Ab).rref()
        inds = np.array(inds)

        # Remueve filas sin pivote
        A = A[inds]
        b = b[inds]

        # Halla todas las posibles combinaciones de matrices cuadradas
        m, n = np.shape(A)
        combinaciones = list(combinations(range(n), m))

        # Inicializa salida
        out = {'Soluciones': [], 'Bases': []}

        # Loop combinaciones
        for comb in combinaciones:

            # Matriz de trabajo
            A_tmp = A[:, comb]

            # Crea la base: Columnas fuera de la base en 0
            A_base = A_or.copy()
            A_base[:, [i for i in range(A.shape[1]) if i not in comb]] = 0

            # Inicaliza vector solución en 0
            x_sol = np.array([0] * A.shape[1], dtype=float)

            # Soluciona
            try:
                # Soluciona para x hallando matriz inversa (solución única)
                x = np.linalg.inv(A_tmp) @ b
                x = x.reshape(-1)  # Cambio de formato

                # Guarda solución
                x_sol[np.array(comb)] = x
                out['Soluciones'].append(x_sol)

                # Guarda base
                out['Bases'].append(A_base)

                # Caso que nos encontremos con una matriz singular (Rango deficiente)
            except Exception as ex:
                # No manejamos el error
                if not handle:
                    out['Soluciones'].append(str(ex))
                    out['Bases'].append(A_base)

                    # Soluciona caso filas linealmente dependientes
                else:
                    # Hallamos soluciónes eliminando filas linealmente ind.
                    try:
                        # Hallamos soluciones básicas de submatriz
                        out2 = self._soluciones_basicas_solucion(A_tmp, b)

                        # Incorporamos en solución anterior
                        for i in range(out2.shape[0]):
                            # Guardamos en x
                            x_sol[np.array(comb)] = out2['Soluciones'][i]

                            # Creamos A y guardamos
                            A_sol = A_base.copy()
                            A_sol[:, comb] = out2['Bases'][i]

                            # Guarda
                            out['Soluciones'].append(x_sol)
                            out['Bases'].append(A_sol)

                            # No se pudo solucionar el error
                    except Exception as ex2:
                        out['Soluciones'].append(str('Singular Matrix'))
                        out['Bases'].append(A_base)

        # Formato dataframe
        out = pd.DataFrame(out)

        # Redondear solución
        out['Soluciones'] = out.apply(self.redondear_valores, axis=1)

        return out

    def calificar_soluciones_basicas(self, A, b, sol_tentativa):
        """
        Función para calificar soluciones básicas.

        Parámetros
        ----------
        A: np.array
          Matriz A (mxn)
        b: np.array
          Vector b (nx1)
        sol_tentativa: dict
          Solución tentativa del estudiante con el formato esperado {'soluciones': [], 'bases':[]}

        """

        # Formato dataframe
        sol_tentativa = pd.DataFrame(sol_tentativa)
        # Redondear solución tentativa
        sol_tentativa['Soluciones'] = sol_tentativa.apply(self.redondear_valores, axis=1)

        # Soluciones básicas correctas
        sol_correcta = self._soluciones_basicas_solucion(A, b)
        # Soluciones en caso de no descomponer las submatrices singulares
        sol_correcta_singular = self._soluciones_basicas_solucion(A, b, handle=False)

        # Numero de soluciones
        n_sol = len(sol_correcta)
        n_sol_min = len(sol_correcta_singular)
        n_sol_tentativa = len(sol_tentativa['Soluciones'])
        n_bases_tentativa = len(sol_tentativa['Bases'])

        # Verificar soluciones dadas
        for i, sol_t in enumerate(sol_tentativa['Soluciones']):
            # Inicializa como falsa
            sol_tentativa_es_correcta = False

            # Caso cuando sol es de una Base Singular
            if type(sol_t) is str:
                base_singular = sol_tentativa['Bases'][i]
                mat_sing = base_singular[:, ~np.all(base_singular == 0, axis=0)]
                if not (np.linalg.det(mat_sing)):
                    sol_tentativa_es_correcta = True

            # Caso cuando sol es de Base No singular
            else:
                # Comparar solucion tentativa con soluciones correctas
                for sol_c in sol_correcta['Soluciones']:
                    # Ignorar resultados de matrices singulares (str)
                    if type(sol_c) is not str:
                        # Verificar que solucion tentativa existe dentro de las correctas
                        if (sol_t == sol_c).all():
                            sol_tentativa_es_correcta = True

            # No se encontró la solución dentro de las soluciones básicas correctas
            assert sol_tentativa_es_correcta, f"{sol_t} NO es solución para el problema A = {A} y b={b}"

        # Verificar número de soluciones
        assert n_sol_tentativa >= n_sol_min, "Las soluciones parecen ser correctas, pero existen más combinaciones de bases para esta matriz, continua trabajando"
        assert n_sol_tentativa >= n_sol, "Las soluciones parecen ser correctas, pero no se le olvide incluir las soluciones singulares o reducir los casos especiales, se pueden llegar a más soluciones!"
        assert not (n_sol_tentativa > n_sol), "No hay tantas soluciones a este problema!"

        print("La soluciones encontradas parecen ser correctas. ¡Buen trabajo!")

    @staticmethod
    def manipulate_ipython(ipython):
        """
        Cambia el traceback para mostrar únicamente los errores obtenidos por Asserts
        En caso de que se encuentre en estra configuración cambia a la configuración inicial
        ___________________________________
        Entrada:
        ipython:          [ipykernel] Kernel utilizado en la sesión actual
        ___________________________________
        Salida:
        toggle_traceback: [function] Función para manipular el traceback

        """

        if 'TRACEDEFAULT' not in globals():
            TRACEDEFAULT = ipython.showtraceback

        def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
                           exception_only=False, running_compiled_code=False):
            """ Oculta el reporte predeterminado de python respecto al error encontrado. """
            etype, value, tb = sys.exc_info()
            value._cause_ = None  # suppress chained exceptions
            return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))

        def toggle_traceback():
            """ Cambia el reporte de traceback """
            if ipython.showtraceback == TRACEDEFAULT:
                ipython.showtraceback = hide_traceback
            else:
                ipython.showtraceback = TRACEDEFAULT

        return toggle_traceback

    @staticmethod
    def redondear_valores(row, n_round=2):
        """ Aproxima cada elemento en la solución. """
        sol = row['Soluciones']
        # Si no es error aproxima
        if not isinstance(sol, str):
            sol = np.around(sol, n_round)
        return sol



