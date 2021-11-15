# Correciones TP3

Corrector: Ernesto


## Nota:

- **Parte 1:** 8
- **Parte 2:** 10
- **Parte 3:** 5



## Comentarios sobre la correccion

### Parte 1:

"Utilizan Ford-Fulkerson para resolver el problema. Lo utilizan 2 veces, para la primera transforman las ciudades en nodos, los viajes en aristas, y la capacidad del viaje es la capacidad de la arista. Para la segunda los nodos siguen siendo las ciudades, las aristas también los viajes, pero la capacidad es de 1. El tema es que el problema no te pedia calcular la cantidad maxima de pasajeros que pueden ir de A a B, que es lo único que se hace con el primer grafo, sino que te pedia saber dónde poner las publicidades, que es lo que se hace con el segundo grafo. Muestran pseudo-código y está bien.

1.2: Muestran cómo es la reducción del problema a un problema de red de flujo, pero no explican porqué es una reducción polinomial. 

1.3: Correcto

1.4: Código correcto

1.5: Correcto"



### Parte 2:

son vértices y los recorridos entre estaciones aristas." esta reduciendo de socorro a set dominante. es decir diciendo que set dominante es igual o mas dificil que el problema del socorro. nada impide entonces que socorro sea muy facil de resolver. no puede afirmar con eso que socorro pertenece a NP-C. Ademas falta mostrar que pertenece a NP (revise como demostrar que un problema pertenece a NP-C)



### Parte 3:

"Reducción polinomial no implica que la ""caja negra"", a la que el problema original se quiere reducir, tiene una complejidad polinomial.

Buena explicación de la importancia de NP-Completo.

3.a: Mal. Si NA soluciona a B, no quiere decir que NA es de tiempo polinomial. Sólo podes asegurar que B es reducible polinomialmente a A

3.b: Bien

3.c.a: Bien

3.c.b: Mal. No se puede afirmar que B es NP-Completo. A es reducible a B, y A es NP-Completo, por lo tanto lo único que se puede afirmar es que B es NP-Hard.
