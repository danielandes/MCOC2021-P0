from scipy.linalg import eigh, inv
from numpy import float32, double, ones
from time import perf_counter
from laplaciana import laplaciana
N=[2,5,10,20,40,50,70,100,400,800,1500,2000,2500,5000,6000]
UsoTiempo=[]
Nlista=[]
for a in range(10):
    for i in N:
        b=ones(i).T
        A=laplaciana(i, double)
        t1=perf_counter()
        Am1=inv(A)
        x=Am1@b
        t2=perf_counter()
        t=t2-t1
        UsoTiempo.append(t)
        Nlista.append(i)




#Creacion del archivo para guardar datos
archivo= open("A_I_d.txt", "w+")
for i in range(len(N*10)):
    archivo.write(str(UsoTiempo[i])+" "+str(Nlista[i])+" "+"\n")
archivo.close()