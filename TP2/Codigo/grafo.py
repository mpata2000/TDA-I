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
  


    def borrar_vertice(self,v):
        if v not in self.vertices:
            return False
    
        for ver in self:
            self.borrar_arista(v,ver)

        del self.vertices[v]
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

    def borrar_arista(self,v,w,peso = 1):
        if not self.estan_unidos(v,w):
            return False
        del self.vertices[v][w]
        if not self.es_dirigido:
            del self.vertices[w][v]
        return True


        if len(self) == 0:
            return None
        return self.vertices[0]


    def adyacentes(self,v):
        return list(self.vertices[v].keys())
  
    def peso_arista(self,v,w):
        if not self.estan_unidos(v,w):
            return None
        return self.vertices[v][w]

  
    def __str__(self):
        cadena = ""
        for v in self.obtener_vertices():
            ady = ",".join(map(str, self.adyacentes(v)))
            cadena += str(v) + ":" + ady + "\n"
        return cadena

  	#Devuelve una lista de tuplas con el peso de la arista, el nodo origen, y el nodo destino
    def obtener_aristas(self):
        aristas = []
        for v in self:
            for a in self.adyacentes(v):
                aristas.append((v,a,int(self.peso_arista(v,a))))

        return aristas

