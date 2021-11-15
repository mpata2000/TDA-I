import sys
import csv


from grafo import Grafo
from funciones_grafo import Johnson

# Crea una matriz de distancias con la primera fila siendo un lista de de nodos
# de hasta donde se mide la distancia y las siguentes filas tienen primero el nodo
# donde se arranca y despues las distancias a los nodos correspondientes
def matriz_de_distancias(diccionario_distancias):

    matriz_a_printear = []

    lista_keys = list(diccionario_distancias.keys())
    lista_keys.insert(0," ")

    matriz_a_printear.append(lista_keys);

    for key, value in diccionario_distancias.items():
        lista_valores = list(value[0].values())

        lista_valores.insert(0, key)

        matriz_a_printear.append(lista_valores)

    return matriz_a_printear

# https://stackoverflow.com/questions/37093510/how-to-print-array-as-a-table-in-python
# Imprime una matriz generada por matriz_de_distancias
def printMatrix(s):
    # Heading
    print("     ", end="")
    for j in range(1, len(s[0])):
        print("%5s " % s[0][j], end="")
    print()
    print("     ", end="")
    for j in range(1, len(s[0])):
        print("------", end="")
    print()


    # Matrix contents
    for i in range(1, len(s)):
        print("%3s |" % s[i][0], end="")
        for j in range(1, len(s[0])):
            cont =  "∞" if (s[i][j] == float("inf")) else s[i][j]

            print("%5s " % cont, end="")
        print() 

# Busca el nodo con la menor suma de distancia de una matriz generada con matriz_de_distancias.
# Devuelve el nodo con menor distancia y la suma de las distancias
def buscar_nodo_con_menores_distancias(matriz):
    mejor_nodo = None
    distancia_mejor_nodo = float("inf")

    for fila in matriz[1:]:
        distancia_actual = sum(fila[1:])
        if distancia_actual < distancia_mejor_nodo:
            mejor_nodo = fila[0]
            distancia_mejor_nodo = distancia_actual

    return mejor_nodo, distancia_mejor_nodo


def main():


    try:
        ruta = sys.argv[1]
        file = open(ruta)
    except IndexError:
        print("No se ingresó ningun archivo.")
        return
    except FileNotFoundError:
        print("No se encontró ningun archivo con ese nombre.")
        return
    except:
        print("Hubo algun error")

   
    

    grafo = Grafo(True)
    try:
        with file as archivo:
            csv_reader = csv.reader(archivo)
            for line in csv_reader:
                ciudadInicio, ciudadFin, distancia = line

                if ciudadInicio not in grafo:
                    grafo.agregar_vertice(ciudadInicio)
                    
                if ciudadFin not in grafo:
                    grafo.agregar_vertice(ciudadFin)

                grafo.agregar_arista(ciudadInicio, ciudadFin, distancia)
    except:
        print("Paso algo inesperado, intente ejecutar el programa nuevamente")
        file.close()
        return

    file.close()
    
    try:
        resolucion_johnson = (Johnson(grafo))
    except ValueError:
        print("El grafo contiene un ciclo negativo. Revise el grafo ingresado e intente nuevamente.")
        return
        


    matriz = matriz_de_distancias(resolucion_johnson)

    printMatrix(matriz)
    print("\nLas distancias son desde los nodos de la primera columna, hasta los nodos de la primera fila.\n")

    ciudad, distancia = buscar_nodo_con_menores_distancias(matriz)

    if (distancia == float("inf")):
        print("No existe ninguna ciudad que se conecte con el resto. Es imposible poner la fabrica en una ciudad, y poder distribuir el producto a todas las ciudades.")
        return


    print("La mejor ciudad para poner la fabrica es: %s con distancia total de %d." % (ciudad, distancia))




main()

