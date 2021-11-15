import queue

from grafo import Grafo


#################################################################
#Genera el camino mas corto en un grafo dirigido y pesado, que puede tener aristas con peso negativo. Recibe un grafo y un nodo para calcular las distancias (desde este a todos los otros), y devuelve un diccionario de distancias (distancia de cada nodo al nodo origen), y de predecesores (el nodo que viene antes si se esta haciendo un camino desde el nodo origen).
# si recibe un grafo con un ciclo negativo se levanta un ValueError
def Bellman_Ford(grafo, nodo_origen):
    distancia = {}
    predecesor = {}

    for v in grafo.obtener_vertices():
        distancia[v] = float("inf")
        predecesor[v] = None

    distancia[nodo_origen] = 0
    predecesor[nodo_origen] = nodo_origen
    
    for i in range(0, len(grafo) -1):
        for u, v, peso in grafo.obtener_aristas():

            if (distancia[u] + peso) < distancia[v]:
                distancia[v] = distancia[u] + peso
                predecesor[v] = u


    for u, v, peso in grafo.obtener_aristas():
        if (distancia[u] + peso) < distancia[v]:
            raise ValueError("Hay un ciclo negativo")

    return distancia, predecesor


#Version original de Dijkstra
#Determina el camino mas corto dado un nodo origen, hacia el resto de los nodos de un grafo pesado. Recibe un grafo y un nodo origen. Devuelve diccionarios equivalentes a los de Bellman-Ford.
def Dijkstra(grafo, nodo_origen):
	dist = {}
	padre = {}

	for v in grafo:
		dist[v]= float("inf")

	dist[nodo_origen] = 0
	padre[nodo_origen] = None
	q = queue.PriorityQueue()
	q.put((0,nodo_origen))
	while not q.empty():
		distancia_v,v = q.get()
		for w in grafo.adyacentes(v):
			if dist[v] + grafo.peso_arista(v,w) < dist[w]:
				dist[w] = dist[v] + grafo.peso_arista(v,w)
				padre[w] = v
				q.put((dist[w],w))
	return dist,padre


#Version 1 de la modificacion de Dijkstra, sin utilizar por ser espacial y temporalmente más complejo por necesitar una copia del grafo original.
#Recibe el grafo original, el grafo modificado por bellman ford, y el nodo desde el que se empieza.
#Develve las distancias respecto al grafo original, y el nodo padre
def Dijkstra_mod(grafo, grafoBF, nodo_origen):
    distBF = {}
    dist = {}
    padre = {}

    for v in grafoBF:
        distBF[v]= float("inf")
        dist[v]= float("inf")

    distBF[nodo_origen] = 0
    dist[nodo_origen] = 0
    padre[nodo_origen] = None
    q = queue.PriorityQueue()
    q.put((0,nodo_origen))
    while not q.empty():
        distancia_v,v = q.get()
        for w in grafoBF.adyacentes(v):
            if distBF[v] + grafoBF.peso_arista(v,w) < distBF[w]:
                distBF[w] = distBF[v] + grafoBF.peso_arista(v,w)
                dist[w] = dist[v] + grafo.peso_arista(v,w)

                padre[w] = v
                q.put((distBF[w],w))
			
    return dist, padre

#Version 2 de la modificacion de Dijkstra, usada actualmente para Johnson
#Recibe el grafo modificado por Bellman-Ford, las distancias desde Q hasta cada nodo obtenido por BF, y el nodo desde el que se empieza.
#Develve las distancias las distancias respecto al grafo original, y el nodo padre 
def Dijkstra_mod_2(grafoBF, distancias_BF, nodo_origen):
    distBF = {}
    dist_originales = {}
    padre = {}

    for v in grafoBF:
        distBF[v]= float("inf")
        dist_originales[v]= float("inf")

    distBF[nodo_origen] = 0
    dist_originales[nodo_origen] = 0
    padre[nodo_origen] = None
    q = queue.PriorityQueue()
    q.put((0,nodo_origen))
    while not q.empty():
        distancia_v,v = q.get()
        for w in grafoBF.adyacentes(v):
            peso_arista_vw = grafoBF.peso_arista(v,w) 

            if distBF[v] + peso_arista_vw < distBF[w]:
                distBF[w] = distBF[v] + peso_arista_vw

                peso_arista_original = peso_arista_vw - distancias_BF[v] + distancias_BF[w]

                dist_originales[w] = dist_originales[v] + peso_arista_original

                padre[w] = v
                q.put((distBF[w],w))
			
    return dist_originales, padre


#Encuentra el camino mas corto entre todos los pares de nodos de un grafo dirigido y pesado. Puede aplicarse sobre un grafo con pesos negativos, pero si se detecta un ciclo negativo se lanza una excepcion. Recibe un grafo. Devuelve un diccionario, donde cada clave es uno de los nodos, y el valor asociado es una tupla con los resultados de Dijkstra para ese nodo.

def Johnson(grafo):
    nuevo_nodo = 'q'
    grafo.agregar_vertice(nuevo_nodo)
    for v in grafo:
        grafo.agregar_arista(nuevo_nodo,v, 0)

    distanciasBF, padresBF = Bellman_Ford(grafo,nuevo_nodo)

    grafo.borrar_vertice("q")

    #grafoBF = grafo.copy()

    for v in grafo:
        for w in grafo.adyacentes(v):
            grafo.vertices[v][w] += (distanciasBF[v] - distanciasBF[w])

    resultados = {}  

    for nodo_origen in grafo:
        distanciasResultado, padresResultado = Dijkstra_mod_2(grafo, distanciasBF, nodo_origen)

        resultados[nodo_origen] = (distanciasResultado, padresResultado)

    return resultados





