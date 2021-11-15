import copy

class Grafo:
    def __init__(self, es_dirigido = False):
        self.es_dirigido = es_dirigido
        self.vertices = {}

    def __len__(self):
        return len(self.vertices)

    def __contains__(self,v):
        return v in self.vertices

    def __iter__(self):
        return iter(self.vertices)

    #Devuelve una copia del grafo, con los valores copiados de manera profunda (osea no por referencia)
    def copy(self):
        nuevoGrafo = Grafo(self.es_dirigido)
        nuevoGrafo.vertices = copy.deepcopy(self.vertices)
        return nuevoGrafo

    def copy_con_pesos(self, new_peso):
        nuevoGrafo = Grafo(self.es_dirigido)
        vertices_nuevos = copy.deepcopy(self.vertices)

        #Itera todos los pesos de aristas, y los asigna como el nuevo peso
        for vertice, vertices_adyacentes in vertices_nuevos.items():
            for vertice_adyacente, peso in vertices_adyacentes.items():

                vertices_nuevos[vertice][vertice_adyacente] = 0 if (peso == 0) else new_peso

        nuevoGrafo.vertices = vertices_nuevos
        return nuevoGrafo

    #Devuelve True si ambos vertices existen, y hay una arista que conecta de V a W
    def estan_unidos(self,v,w):
        if v not in self.vertices or w not in self.vertices:
            return False
        if w not in self.vertices[v]:
            return False
        return True

    #Devuelve lista de vertices
    def obtener_vertices(self):
        return list(self.vertices.keys())

    def agregar_vertice(self,v):
        if v in self.vertices:
            return False
        self.vertices[v] = {}
        return True

    #Si uno de los vertices no esta en el grafo, o ambos vertices son el mismo, no hace nada
    #Si la arista existe, tampoco, solo agrega aristas inexistentes
    def agregar_arista(self,v,w,peso = 1):
        peso = int(peso)

        if v not in self.vertices or w not in self.vertices:
            return False
        if v == w:
            return False
        if self.estan_unidos(v,w):
            return False
          
        self.vertices[v][w] = peso
        if not self.es_dirigido:
            self.vertices[w][v] = peso
        return True

  

    #Borra vertice, y respectivas aristas salientes y entrastes
    def borrar_vertice(self,v):
        if v not in self.vertices:
            return False
    
        for ver in self:
            self.borrar_arista(ver,v)

        del self.vertices[v]
        return True
    
    
    def borrar_arista(self,v,w):
        if not self.estan_unidos(v,w):
            return False

        vertice_inicial = self.vertices[v]
        vertice_final = self.vertices[w]

        vertice_inicial.pop(w)

        if not self.es_dirigido:
            vertice_final.pop(v)

        return True


    def cambiar_peso(self,v,w,peso):
        if v not in self.vertices or w not in self.vertices:
            print("no estan")
            return False
        if v == w:
            return False
        if not self.estan_unidos(v,w):
            return False

        self.vertices[v][w] = peso


    def adyacentes(self,v):
        return list(self.vertices[v].keys())
  
    def peso_arista(self,v,w):
        if not self.estan_unidos(v,w):
            return None
        return self.vertices[v][w]

    def peso(self, v, w):
        return self.peso_arista(v,w)

    def set_unilateralmente_conexo_desde(self, v):

        visitados = set()
        
        set_conexo = self.__set_unilateralmente_conexo_desde_recursivo__(v, visitados)

        return set_conexo
        
    def __set_unilateralmente_conexo_desde_recursivo__(self, v, visitados):
        set_conexo = {v}


        for nodo_vecino in self.adyacentes(v):
            if not nodo_vecino in visitados:
                visitados.add(nodo_vecino)
                set_ext = self.__set_unilateralmente_conexo_desde_recursivo__(nodo_vecino, visitados)
                set_conexo.update(set_ext)

        return set_conexo


  
    def __str__(self):
        matriz_distancias = self.__matriz_de_distancias__(self.vertices)
        return self.__stringMatrix__(matriz_distancias)


    def __repr__(self):
        return self.__str__()

  	#Devuelve una lista de tuplas con el peso de la arista, el nodo origen, y el nodo destino
    def obtener_aristas(self):
        aristas = []
        for v in self:
            for a in self.adyacentes(v):
                aristas.append((v,a,int(self.peso_arista(v,a))))

        return aristas



    # Crea una matriz de distancias con la primera fila siendo un lista de de nodos
    # de hasta donde se mide la distancia y las siguentes filas tienen primero el nodo
    # donde se arranca y despues las distancias a los nodos correspondientes
    def __matriz_de_distancias__(self, diccionario_distancias):

        matriz_a_printear = []

        lista_keys = list(diccionario_distancias.keys())
        lista_keys.insert(0," ")

        matriz_a_printear.append(lista_keys)

        for desde in lista_keys[1:]:
            lista_valores = [desde]

            for hasta in lista_keys[1:]:
                dic_origen = diccionario_distancias.get(desde)
                distancia = dic_origen.get(hasta, float("inf"))

                if (desde == hasta):
                    distancia = 0
                lista_valores.append(distancia)

            matriz_a_printear.append(lista_valores)


        return matriz_a_printear

    # Modificacion de:
    # https://stackoverflow.com/questions/37093510/how-to-print-array-as-a-table-in-python
    # Devuelve un string listo para poder imprimir por terminal
    def __stringMatrix__(self, s):
        string = ""
        # Heading
        string += "     "
        for j in range(1, len(s[0])):
            string += "%5s " % s[0][j]
        string+= "\n"
        string += "     "
        for j in range(1, len(s[0])):
            string += "------"
        string += "\n"


        # Matrix contents
        for i in range(1, len(s)):
            string += "%3s |" % s[i][0]
            for j in range(1, len(s[0])):
                cont = "∞" if (s[i][j] == float("inf")) else s[i][j]

                string += "%5s " % cont
            string+= "\n"

        return string

            
