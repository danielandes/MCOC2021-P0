from scipy.linalg import eigh, inv, solve
from numpy import float32, double, ones
from time import perf_counter
from laplaciana import laplaciana
N=[2,5,10,20,40,50,70,100,400,800,1500,2000]
UsoTiempo=[]
Nlista=[]
for a in range(10):
    for i in N:
        A=laplaciana(i, float32)
        t1=perf_counter()
        w,h=eigh(A, driver="evx", overwrite_a=False)
        t2=perf_counter()
        t=t2-t1
        UsoTiempo.append(t)
        Nlista.append(i)





#Creacion del archivo para guardar datos
archivo= open("B_V_F_f.txt", "w+")
for i in range(len(N*10)):
    archivo.write(str(UsoTiempo[i])+" "+str(Nlista[i])+" "+"\n")
archivo.close()