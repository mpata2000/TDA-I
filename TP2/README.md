# Correciones TP2

Corrector: Lucas

## Notas:

- Parte 1: 8
- Parte 2: 9

## Comentarios a las correcciones:

### Parte 1:

Para la justificación de optimalidad no se tiene en cuenta la primera parte del algoritmo donde se usa Bellman-Ford

No se explica qué ocurre luego de aplicar el algoritmo de Dijkstra

No se justifican por qué cada algoritmo tiene la complejidad explicitada

¿Johnson podría ser levemente peor que Floyd en un grafo totalmente disperso por el primer término de la complejidad?. Muy bueno el análisis

¿Cuál es el nodo que elegirían para colocar la fábrica en el ejemplo?



#### Ejecución del programa:

La complejidad de BellmanFord quedó de O(V^2*E)

Muy bueno el código y muy prolijo (una opinión puramente mía, no pondría más de 2 saltos de líneas)

Buena idea la adaptación de Dijkstra



## Parte 2:

No me terminó de convencer la descripción de elección de candidatos para Greedy ya que es un poco particular a algún algoritmo del tipo greedy pero no genérica. El resto está muy bien.

División y conquista no se caracteriza necesariamente por la memorización de soluciones

No se termina de entender esta frase “En casos donde la problemática no sea de optimización podríamos perder más tiempo en tratar de demostrar que nuestra solución greedy verdaderamente nos entrega un solución óptima”

La justificación del 2.2 es correcta
