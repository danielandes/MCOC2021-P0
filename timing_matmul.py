from numpy import zeros, float64
from time import perf_counter
import matplotlib.pylab as plt
N=[1,5,10,20,40,50,80,100,150,200,300,500,1000,1500,2000,5000,10000] #,2000,5000,10000

UsoMemoria=[]
UsoTiempo=[]
Nlista=[]
for a in range(10):
    for i in N:
        A=zeros((i,i), dtype=float64)+1
        B=zeros((i,i), dtype=float64)+2
        t1=perf_counter()
        C=A@B
        t2=perf_counter()
        t=t2-t1
        UsoTiempo.append(t)
        memoria= A.nbytes + B.nbytes + C.nbytes
        UsoMemoria.append(memoria)
        Nlista.append(i)



#Creacion del archivo para guardar datos
archivo= open("usorecursos.txt", "w+")
for i in range(len(N*10)):
    archivo.write(str(UsoMemoria[i])+" "+str(UsoTiempo[i])+" "+str(Nlista[i])+" "+"\n")
archivo.close()
