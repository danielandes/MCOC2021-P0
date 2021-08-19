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
  * np.half se intenta promover a np.single pero arroja el error "array type float16 is unsupported in linalg" en la inversion.
  * np.single se comporta como 32bits
  * np.double se comporta como 64bits
  * np.longdouble se intenta degradar a np.double pero arroja el error "array type float64 is unsupported in linalg" en la inversion
* Entre los tipos de datos se observa que la libreria de scipy es mas eficiente que numpy en el uso de CPU y tiempo necesario para realizar la inversion de las matrices, asi tambien se observa que el half de scipy se promueve a single para la matriz invertida mientras que el longdouble de scipy se degrada a double para la matriz original e invertida debido al funcionamiento de la libreria y mi sistema. Entre
* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.
  * Numpy es generalmente utilizado para calculos "basicos" de manera rapida, sin embargo la libreria scipy contiene mas algoritmos y de esta manera puede que contenga un mejor algoritmo que numpy para invertir las matrices de manera aun mas eficiente. A traves de los datos obtenidos resulta claro que sus algoritmos son diferentes, siendo el de scipy mas rapido, por lo que pareciese que numpy utiliza el algoritmo de eliminacion gaussiana de dificultad O(n^3) mientras que scipy strassen con dificultad O(n^2,807) ya que la diferencia de tiempos no parece tan grande como para ser una diferencia que involucre el algoritmo de coppersmith-winograd de dificultad O(n^2,373)
* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas.
  * Influira en la eficiencia de los calculos, el cache permitira realizar calculos con memoria mas cercana y el adecuado trabajo en paralelo permitira utilizar todos los nucleos al maximo. En este caso la principal diferencia se observa entre las corridas con numpy y scipy. Con numpy se observa que la CPU alcanza cargas maximas de 70% mientras que con scipy se alcanzan 99% de carga,asi tambien se observa que las corridas con scipy son mas rapidas que las de numpy (diferencias mejor observables en los datos.txt) y el uso de memoria (observable a traves de task manager) de numpy es mayor al de scipy siendo que teoricamente las matrices utilizan la misma memoria para guardarse. Por lo que scipy aprovecha mejor los nucleos en trabajo en paralelo y sus algoritmos de inversion son mas eficientes que numpy.
