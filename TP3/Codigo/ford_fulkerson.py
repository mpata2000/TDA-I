import queue

from grafo import Grafo

#A partir de un grafo, y un set de nodos de ese grafo; devuelve las aristas que conectan a un nodo del set, a un nodo que no se encuentra en el set
def calcular_aristas_corte_minimo(grafo, grafo_residual, s):
    set_nodos_lado_fuente = grafo_residual.set_unilateralmente_conexo_desde(s) #Set que contiene a los nodos que se pueden acceder luego de augmentar el grafo 

    conexiones = []

    for nodo in set_nodos_lado_fuente:
        if nodo not in grafo:
            raise IndexError("Nodo perteneciente al set no existe en el grafo al que el set referencia")

        for nodo_vecino in grafo.adyacentes(nodo):
            if nodo_vecino not in set_nodos_lado_fuente:
                conexiones.append([nodo, nodo_vecino])

    return conexiones




def actualizar_grafo_residual(grafo_residual, u, v, valor):
    peso_anterior = grafo_residual.peso(u,v)
    peso_anterior_residual = grafo_residual.peso(v,u)

    if peso_anterior <= valor:      #si el nuevo peso es menor a 0
        grafo_residual.borrar_arista(u,v)
    else:
        grafo_residual.cambiar_peso(u,v,peso_anterior - valor)
    
    if not grafo_residual.estan_unidos(v,u):    
        grafo_residual.agregar_arista(v,u, valor)
    
    else:
        grafo_residual.cambiar_peso(v, u, peso_anterior_residual + valor)


#consigue el minimo peso de las aristas involucrados en el camino (lista de vertices)
def min_peso(grafo, camino):
    min_peso = float('inf')

    for i in range(len(camino)-1):
      peso = grafo.peso_arista(camino[i],camino[i+1])
      if peso < min_peso:
        min_peso = peso

    return min_peso


#Recibe un grafo, el nombre del nodo inicial (nodo_actual), y el nodo objetivo (al que se quiere encontrar el camino). Devuelve una lista con los nodos
#Con el objetivo en la posicion 0; y el nodo inicial en la posicion N
def dfs(grafo, nodo_actual, objetivo, visitados = None):
    if visitados == None: #Para que la primera llamada recursiva no tenga que enviar el set
        visitados = set()

    if nodo_actual in visitados:    #Devuelve nada (lista vacia) si se ya paso por ese nodo
        return []

    if nodo_actual == objetivo:     #Llegó al objetivo, empieza a armar la lista.
        visitados.add(nodo_actual)
        return [nodo_actual]

    visitados.add(nodo_actual)  #Agrega el nodo actual al set de nodos visitados
    for vecino in grafo.adyacentes(nodo_actual):    #Se busca sigue el DFS en cada uno de los vecinos del nodo actual
        resultado = dfs(grafo, vecino, objetivo,  visitados)    

        if resultado:
            resultado.append(nodo_actual)
            return resultado
    
    return []       #En el caso de que no se haya logrado alcanzar el nodo objetivo, se devuelve una lista vacia
           

#Devuelve en un vector, un camino desde el nodo S, hasta el nodo T en el grafo. en la posicion [0] esta S, y el la posicion [n] esta T.
#Si no encuentra ningun camino, devuelve un vector vacío
def obtener_camino(grafo, s, t):
    camino = dfs(grafo, s, t)
    return camino[::-1]
    

def flujo_ford_fulkerson(grafo, s, t):
    capacidad_maxima = 0
    grafo_residual = grafo.copy()


    camino = obtener_camino(grafo_residual,s,t) 
    while camino:
        capacidad_residual_camino = min_peso(grafo_residual, camino) #peso minimo de camino (cuello de botella)
        capacidad_maxima += capacidad_residual_camino
    
        nodo_anterior = None

        for nodo_actual in camino:
            if (nodo_anterior != None): #Si nodo anterior es None, no se ejecuta la actualizacion del grafo, para poder tener una arista entre nodo actual y anterior.
                actualizar_grafo_residual(grafo_residual, nodo_anterior, nodo_actual, capacidad_residual_camino)

            nodo_anterior = nodo_actual


        camino = obtener_camino(grafo_residual,s,t)

    return capacidad_maxima, grafo_residual
