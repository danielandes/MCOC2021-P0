from numpy import zeros, float64
from time import perf_counter
import matplotlib.pylab as plt
#Recuperacion de datos desde el archivo

Nombres= ["recursos_inv_caso_1_single.txt","recursos_inv_caso_1_double.txt","recursos_inv_caso_2_half.txt","recursos_inv_caso_2_single.txt","recursos_inv_caso_2_double.txt","recursos_inv_caso_2_longdouble.txt","recursos_inv_caso_3_half.txt","recursos_inv_caso_3_single.txt","recursos_inv_caso_3_double.txt","recursos_inv_caso_3_longdouble.txt"] #["recursos_inv_caso_1_single.txt","recursos_inv_caso_1_half.txt"]
for nombre in Nombres:
    Memoriatxt=[]
    Tiempotxt=[]
    Ntxt=[]
    lectura= open(nombre, "r")
    for i in lectura:
        
        valores=i.split(" ")
        valores.pop()
        Memoriatxt.append(float(valores[0]))
        Tiempotxt.append(float(valores[1]))
        Ntxt.append(float(valores[2]))
    lectura.close()
    a=len(Ntxt)/10
    a=int(a)
        
    #Graficar
    xlabels= ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
    xN=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    ytiempolabels= ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
    ytiempoT=[(10**-4),(10**-3),(10**-2),(10**-1),(1),(10),(60),(600)]
    ymemorialabels= ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
    ymemoriaB= [(10**3),(10**4),(10**5),(10**6),(10**7),(10**8),(10**9),(10**10)]
    
    
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title(nombre)
    for i in range(10):
        plt.loglog(Ntxt[a*i:a*i+a],Tiempotxt[a*i:a*i+a], marker="o")
    plt.xticks(xN,xlabels, rotation=60, visible=False)
    plt.grid(True)
    plt.yticks(ytiempoT,ytiempolabels)
    plt.ylabel("Tiempo transcurrido")
    
    
    plt.subplot(2,1,2)
    plt.loglog(Ntxt,Memoriatxt, marker="o")
    plt.xticks(xN,xlabels, rotation=60)
    plt.yticks(ymemoriaB,ymemorialabels)
    plt.grid(True)
    plt.axhline(y=0.8*10**10, linestyle="--", color="black")
    plt.ylabel("Uso memoria")
    plt.xlabel("Tamano matriz N")
    plt.show()