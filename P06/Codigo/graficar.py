  
from numpy import zeros, float64
from time import perf_counter
import matplotlib.pylab as plt
#Recuperacion de datos desde el archivo

Nombres= ["solve_llena.txt","solve_dispersa.txt","inv_llena.txt","inv_dispersa.txt"]
for nombre in Nombres:
    Ensamblaje=[]
    Solucion=[]
    Ntxt=[]
    lectura= open(nombre, "r")
    for i in lectura:
        
        valores=i.split(" ")
        valores.pop()
        Ensamblaje.append(float(valores[0]))
        Solucion.append(float(valores[1]))
        Ntxt.append(float(valores[2]))
    lectura.close()
    a=len(Ntxt)/10
    a=int(a)
    
    suma=0
    suma2=0
    minimoEns=5
    minimoSol=5
    for j in range(10):
            suma+=Ensamblaje[a*j]
            suma2+=Solucion[a*j]
            if Ensamblaje[a*j]< minimoEns: minimoEns=Ensamblaje[a*j]
            if Solucion[a*j]< minimoSol: minimoSol=Solucion[a*j]
    promedioEns=suma/10
    promedioSol=suma/10
    maximoEns=max(Ensamblaje)
    maximoSol=max(Solucion)
    if maximoEns>Ensamblaje[-1]: maximoEns= Ensamblaje[-1]
    if maximoSol>Solucion[-1]: maximoSol= Solucion[-1]
        
    #Graficar
    xlabels= ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
    xN=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    ytiempolabels= ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
    ytiempoT=[(10**-4),(10**-3),(10**-2),(10**-1),(1),(10),(60),(600)]
    ymemorialabels= ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
    ymemoriaB= [(10**3),(10**4),(10**5),(10**6),(10**7),(10**8),(10**9),(10**10)]
    if nombre=="solve_dispersa.txt":
        xlabels= ["10","20","50","100","200","500","1000","2000","5000","10000","20000","30000","40000"]
        xN=[10,20,50,100,200,500,1000,2000,5000,10000,20000,30000,40000]
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.title(nombre)
    for i in range(10):
        plt.loglog(Ntxt[a*i:a*i+a],Ensamblaje[a*i:a*i+a], marker="o", color="gray")
    plt.plot([Ntxt[0],Ntxt[-1]],[maximoEns,maximoEns], "--", label="Constante")
    for i in range(4):
        l=[Ntxt[0],Ntxt[-1]]
        l2=[minimoEns/Ntxt[-1]**i, maximoEns]
        plt.plot(l,l2, "--",label="O(N"+str(i+1)+")")

    plt.xticks(xN,xlabels, rotation=60, visible=False)
    plt.grid(True)
    plt.yticks(ytiempoT,ytiempolabels)
    plt.ylabel("Tiempo Ensamblaje")
    plt.ylim([10**-6,600])
    plt.legend(loc="upper left")
    
    plt.subplot(2,1,2)
    for i in range(10):
        plt.loglog(Ntxt[a*i:a*i+a],Solucion[a*i:a*i+a], marker="o", color="gray")
    plt.plot([Ntxt[0],Ntxt[-1]],[maximoSol,maximoSol], "--", label="Constante")
    for i in range(4):
        l=[Ntxt[0],Ntxt[-1]]
        l2=[minimoSol/Ntxt[-1]**i, maximoSol]
        plt.plot(l,l2, "--", label="O(N"+str(i+1)+")")

    plt.xticks(xN,xlabels, rotation=60)
    plt.grid(True)
    plt.yticks(ytiempoT,ytiempolabels)
    plt.grid(True)
    plt.ylabel("Tiempo Solucion")
    plt.xlabel("Tamano matriz N")
    plt.ylim([10**-6,600])
    plt.legend(loc="upper left")
    plt.show()