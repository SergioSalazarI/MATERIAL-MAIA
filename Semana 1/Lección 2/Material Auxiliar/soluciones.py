import numpy as np

def es_ortogonal_sol(v_list:list):
    """ 
    Determina si un conjunto dado es ortogonal
    ___________________________________
    Entrada:
    v_list:   [list] Conjunto de vectores
    ___________________________________
    Salida:
    ortogonal: [boolean] True si el conjunto es ortogonal, False si no es ortogonal
    """
    # Variable booleana que se retorna al final del código
    ortogonal = True
    
    # Primer indice del recorrido
    i = 0
    
    # Recorrido sobre los elementos de v_list.
    while (i < len(v_list)-1 and ortogonal == True):

    # Recorrer a partir del siguiente elemento
        j = i+1
    
    # Recorrer los vectores siguientes al vector actual
        while j< len(v_list):
            # Calcular el producto punto entre el vector en la posición i y el vector en la posición j.
            dot_product = np.dot(v_list[i],v_list[j])
            
    # Determinar si el conjunto es ortogonal o no
            if dot_product != 0:
                ortogonal = False
                break

    # Avance del indice j  
            j = j+1

    # Avance del indice i
        i = i+1
    return ortogonal


def gram_schmindt_sol(v_list:list):
    """
    Recibe un conjunto de vectores linealmente independientes 
    y obtiene un conjunto ortonormal por medio del algoritmo de gram-schimdt
    ___________________________________
    Entrada:
    v_list: [list] Lista de los elementos del conjunto \beta'
    ___________________________________
    Salida:
    v_list_gs: [list]  Lista de los vectores resultantes del algoritmo de gram-schimdt
    """

    # Lista que contiene los elementos del conjunto ortonormal final.
    v_list_gs = []

    # Se define el vector de ceros.
    vector_cero = np.zeros(len(v_list[0]))

    # Recorrido de los elementos de v_list
    for i in range(0,len(v_list)):

        # Elemento actual de la iteración (v_i).
        actual = np.array(v_list[i])

        # Vector que contiene la suma de las proyecciones de 'actual' sobre los elementos de 'v_list_gs'
        proyeccion = vector_cero

        # Rcorrido de los elementos del conjunto ortogonal
        for j in range(0,len(v_list_gs)):
            # Elemento del conjunto ortogonal parcial
            aj = np.array(v_list_gs[j])

            # Actualización del vector 'proyeccion'
            proyeccion = proyeccion+(np.dot(actual,aj)/np.dot(aj,aj))*aj

        # Calcular el siguiente vector del conjunto ortonormal
        a_siguiente = actual - proyeccion

        # Determina si el vector resultante de la iteración (i) es el vector cero.
        if (a_siguiente!=vector_cero).any():
            # Se agrega el elemento despues de normalizarlo.
            v_list_gs.append(a_siguiente/np.linalg.norm(a_siguiente))

    # Transformar cada elemento de v_list_gs de formato array a formato de lista (list).
    for i in range(len(v_list_gs)):
        v_list_gs[i] = v_list_gs[i].tolist()

    # Retornar la lista con los elementos resultantes del algoritmo de Gram-Schmidt
    return v_list_gs
