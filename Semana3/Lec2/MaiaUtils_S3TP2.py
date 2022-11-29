
# Librerias
import numpy as np
import math as m
import sys


class MaiaUtils:

    @staticmethod
    def _probabilidad_bayesiana_solucion(y, data, prior=None):
        """
        Calcula la función de probabilidad de que una observacion y, dada la data D,
        pertenezca a la clase C.
        i.e. P(y∈C|D)
        ___________________________________
        Entrada:
        y:      [numpy.ndarray] Nueva observación de la cual se desea conocer la probabilidad (1x2).
        data:   [numpy.ndarray] Matriz con los valores de los datos previamente observados (nx2).
        prior:  [numpy.ndarray] Tamaño o varianza de la creencia previa para cada una de las probabilidades (1x2).
        ___________________________________
        Salida:
        p         [float32] Probabilidad de que la observacion pertenezca a la clase C.
        """

        r1 = np.max(data[:, 0]) - np.min(data[:, 0])
        r2 = np.max(data[:, 1]) - np.min(data[:, 1])

        if np.min(data[:, 0]) < y[0] and y[0] < np.max(data[:, 0]):
            d1 = 0
        else:
            d1 = np.min(abs(y[0] - data[:, 0]))

        if np.min(data[:, 1]) < y[1] and y[1] < np.max(data[:, 1]):
            d2 = 0
        else:
            d2 = np.min(abs(y[1] - data[:, 1]))

        den = (1 + d1 / r1) * (1 + d2 / r2)
        n = len(data)

        if prior is not None:
            num = m.exp(-(d1 / prior[0] + d2 / prior[1]))
        else:
            num = 1

        p = num / (den ** (n - 1))

        return p

    def calificar_funcion_probabilidad(self, p, data, Y1, Y2, prior=None):
        """
        Función para calificar soluciones básicas.

        """
        # Se definen los límites y la resolución de la gráfica
        p_sol = np.zeros((len(Y1), len(Y2)))

        # Se calculan las probabilidades para cada punto en el espacio
        for i, y1 in enumerate(Y1):
            for j, y2 in enumerate(Y2):
                observacion = [y1, y2]
                if prior is None:
                    p_sol[i][j] = self._probabilidad_bayesiana_solucion(observacion, data)
                else:
                    p_sol[i][j] = self._probabilidad_bayesiana_solucion(observacion, data, prior)

        if np.sum(p) == 0:
            print("Las probabilidades en todos los puntos son cero! Complete la función para calcular los valores")

        if np.max(p) > 1:
            print("Los valores de probabilidad parecen ser mayores a 1! Esto no es posible, revise la implementación")

        if np.max(p) < 0:
            print("Los valores de probabilidad parecen ser menores a 0! Esto no es posible, revise la implementación")

        if np.max(p - p_sol) < 0.001:
            print("La función de probabilidad es correcta ¡Buen trabajo!")
        else:
            print("Los valores de probabilidad parecen no ser correctos"
                  "\n¡Revise la función implementada!")

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




