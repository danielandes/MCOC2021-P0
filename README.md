# MCOC2021-P0

# Mi computador principal

* Marca/modelo: -
* Tipo: Escritorio
* Año adquisición: -
* Procesador:
  * Marca/Modelo: Intel Core i5-10400F
  * Velocidad Base: 2.90 GHz
  * Velocidad Máxima: 4.30 GHz
  * Numero de núcleos: 6
  * Humero de hilos: 12
  * Arquitectura: Comet Lake
  * Set de instrucciones:   MMX, SSE, SSE2, SSE3, SSE4.1, SSE 4.2, EM64T, VT-x, AES, AVX, AVX2, FMA3
* Tamaño de las cachés del procesador
  * L1d: 32KB x6
  * L1i: 32KB x6
  * L2: 256KB x6
  * L3: 12MB
* Memoria 
  * Total: 16 GB
  * Tipo memoria: DDR4
  * Velocidad 2666 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Nvidia GeForce GTX 960
  * Memoria dedicada: 4 GB
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: TOSHIBA
  * Tipo: HDD
  * Tamaño: 1TB
  * Particiones: 4


  
* Dirección MAC de la tarjeta wifi: 3C-7C-3F-B9-A1-77
* Dirección IP (Interna, del router): 192.168.0.9
* Dirección IP (Externa, del ISP): 190.160.0.15
* Proveedor internet: VTR

# Desempeño MATMUL
![ImagenProducida](https://user-images.githubusercontent.com/88337429/128420566-253e2029-4ec9-4069-bfd6-27ba2f8cd176.png)


* ¿Cómo difiere del gráfico del profesor/ayudante?
  * Se puede observar que en las zonas intermedias del grafico se obtuvieron tiempos menores a los del profesor/ayudante, mientras que los iniciales presentan un salto bastante notable despues de la primera corrida, y para las matrices mas grandes no se presenta mucha diferencia.
* ¿A qué se pueden deber las diferencias en cada corrida?
  * La diferencia observada entre la primera corrida y las subsiguientes se puede deber a que al ejecutarse la matriz pequeña en las iteraciones, esta venia justo despues de la mas grande de la iteracion anterior, pudiendo realentizarse por una falta de memoria RAM al momento iniciar la siguiente iteracion (Si bien el sistema cuenta con 16GB RAM, gran parte ya se encontraba utilizada antes de ejecutar el programa por ultima vez), en el peor de los casos haciendo paginacion o tal vez simplemente no se encontraban disponibles los caches del cpu, que es la que podria afectar mas la eficiencia de procesos pequeños.
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  * Si bien el espacio reservado para las matrices depende del tamaño N*N de estas para quedarse y utilizarse desde la RAM, el cual se ve linealmente en el grafico loglog, el proceso de *MULTIPLICAR* estas matrices guardadas en la RAM que se vuelve cada vez mas complejo tambien teoricamente dependiente de N*N, no es lineal debido a que la cpu tarda un tiempo, si bien muy pequeño, en iniciar el proceso que se encontraba en cola, en este caso la multiplicacion de la matriz, mientras que se observa lineal hacia el final del grafico debido a que este tiempo que tarda en iniciarlo se vuelve casi despreciable al compararse con lo que tarda la multiplicacion en si.
* ¿Qué versión de python está usando?
  * 3.7
* ¿Qué versión de numpy está usando?
  * 1.18.1
* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 
  * Se usan los 6 nucleos disponibles para mayor eficiencia
  * ![recursos2](https://user-images.githubusercontent.com/88337429/128415884-9c5adc74-b433-4ff7-abcd-f0627707b0c5.PNG)

# Desempeño INV
* En mi sistema:
  * np.half arroja el error "array type float16 is unsupported in linalg" en la inversion de numpy, mientras que para scipy la matriz invertida es promovida a single mientras que la original se mantiene como half.
  * np.single se comporta como 32bits para numpy y scipy
  * np.double se comporta como 64bits para numpy y scipy
  * np.longdouble se intenta trabajar como double pero arroja el error "array type float64 is unsupported in linalg" en la inversion de numpy, mientras que para scipy las matrices invertida y original se trabaja como 64bits debido al sistema y la libreria.
* Entre los tipos de datos se observa que la libreria de scipy es mas eficiente que numpy en el uso de CPU y tiempo necesario para realizar la inversion de las matrices, asi tambien se observa que el half de scipy se promueve a single para la matriz invertida mientras que la longdouble de scipy se degrada a double para la matriz original e invertida debido al funcionamiento de la libreria y mi sistema. Mientras que para las diferencias entre scipy con overwrite_a=False/True se obtienen resultados donde a veces uno es mas rapido que el otro, la documentacion informa que podria suponer una diferencia en rendimiento, lo cual no ocurre para este caso.
* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.
  * Numpy es generalmente utilizado para calculos "basicos" de manera rapida, sin embargo la libreria scipy contiene mas algoritmos y de esta manera puede que contenga un mejor algoritmo que numpy para invertir las matrices de manera aun mas eficiente. A traves de los datos obtenidos resulta claro que sus algoritmos son diferentes, siendo el de scipy mas rapido, por lo que pareciese que numpy utiliza el algoritmo de eliminacion gaussiana de dificultad O(n^3) mientras que scipy strassen con dificultad O(n^2,807) ya que la diferencia de tiempos no parece tan grande como para ser una diferencia que involucre el algoritmo de coppersmith-winograd de dificultad O(n^2,373)
* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas.
  * Influira en la eficiencia de los calculos, el cache permitira realizar calculos con memoria mas cercana y el adecuado trabajo en paralelo permitira utilizar todos los nucleos al maximo. En este caso la principal diferencia se observa entre las corridas con numpy y scipy. Con numpy se observa que la CPU alcanza cargas maximas de 70% mientras que con scipy se alcanzan 99% de carga, asi tambien se observa que las corridas con scipy son mas rapidas que las de numpy (diferencias mejor observables en los datos.txt) y el uso de memoria (observable a traves de task manager) de numpy es mayor al de scipy siendo que teoricamente las matrices utilizan la misma memoria para guardarse. Por lo que scipy aprovecha mejor los nucleos en trabajo en paralelo y sus algoritmos de inversion son mas eficientes que numpy.

# Desempeño SOLVE y EIGH
* ¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo? 
  * Para A, se observa que el invertir la matriz para luego hacer matmul consume mas tiempo que cualquier opcion de solve para matrices mas grandes que 50x50 tanto para datos tipo float como double. Siendo el uso de assume_a="pos" el mas rapido para ambos tipos de datos tanto para matrices pequeñas como grandes, el cual tiene un comportamiento similar a assume_a="sym" hasta que se empieza a trabajar con matrices mas grandes. Entre los tipos de dato float y double se observa que para todos los casos float es mas rapido, lo cual es de esperar ya que se requiere trabajar con menos bits. Cabe destacar que la diferencia de tipo de dato fue mas notable para el caso I, donde double llego a tardar el doble que float, mientras que para los otros casos las diferencias no son mayores al 30%.
  * Para B, se observa que los casos mas lentos corresponden a II y V con sus variantes, mientras que los casos I, III y IV entregan resultados similares, siendo III_float el mas rapido sin mejoras de desempeño observables por el uso de overwrite. 
* ¿Qué algoritmo gana (en promedio) en cada caso?
  * Para A gana el caso III assume_a="pos" con dato float para todos los tamaños de matrices utilizados.
  * Para B gana el caso III driver="evd" con dato float sin diferencia entre overwrite_a=True/false.
  * Aunque se debe tener en cuenta que al utilizar menos bits se pierde precision en el resultado.
* ¿Depende del tamaño de la matriz?
  * Para los casos de A se observa que los comportamientos varian bastante entre ellos para matrices menores a 1000x1000, siendo algunos mas rapidos para tamaños menores y luego mas lentos que otros casos para tamaños mayores.
  * En el caso de B se observa un comportamiento similar a lo largo de las corridas.
 * ¿A que se puede deber la superioridad de cada opción?
   * Se debe a las estrategias que utilizan los algoritmos que llama cada funcion para la resolucion de los problemas, donde algunas seran mas optimas que otras dependiendo de los casos, asi tambien que tan optimizadas son las librerias para utilizar el CPU. Por ejemplo en los casos II y V de B, la CPU se encontraba con carga en uno o dos nucleos la mayoria del tiempo, coincidiendo con que estos casos fueron los mas lentos. Mientras que para el caso III de A se utilizaron todos los nucleos a menor carga que los otros casos de A, y aun asi logro mejor desempeño ya que el algoritmo requiere menos calculos pero sigue aprovechando todos los nucleos.
