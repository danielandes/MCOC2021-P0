from numpy import double
from time import perf_counter#from laplaciana import laplaciana
import scipy.sparse as sparse
from laplaciana import laplaciana
N=[2,5,10,20,40,50,80,100,150,200,300,500,1000,1500,2000,2500,3000,4000,5000,6000,8000,9000,10000] #,2000,5000,10000


UsoTiempo_ens=[]
UsoTiempo_sol=[]
Nlista=[]
for a in range(10):
    for i in N:
        t1=perf_counter()
        A=laplaciana(i, double)
        B=laplaciana(i, double)
        t2=perf_counter()
        C=A@B
        t3=perf_counter()
        t_ensamblaje=t2-t1
        t_solucion=t3-t2
        UsoTiempo_ens.append(t_ensamblaje)
        UsoTiempo_sol.append(t_solucion)
        Nlista.append(i)
        print(len(A))



#Creacion del archivo para guardar datos
archivo= open("datos_llena.txt", "w+")
for i in range(len(N*10)):
    archivo.write(str(UsoTiempo_ens[i])+" "+str(UsoTiempo_sol[i])+" "+str(Nlista[i])+" "+"\n")
archivo.close()

UsoTiempo_ens2=[]
UsoTiempo_sol2=[]
Nlista2=[]
for a in range(10):
    for i in N:
        t1=perf_counter()
        A=sparse.csr_matrix(laplaciana(i, double))
        B=sparse.csr_matrix(laplaciana(i, double))
        t2=perf_counter()
        C=A@B
        t3=perf_counter()
        t_ensamblaje=t2-t1
        t_solucion=t3-t2
        UsoTiempo_ens2.append(t_ensamblaje)
        UsoTiempo_sol2.append(t_solucion)
        Nlista2.append(i)



#Creacion del archivo para guardar datos
archivo= open("datos_dispersa.txt", "w+")
for i in range(len(N*10)):
    archivo.write(str(UsoTiempo_ens2[i])+" "+str(UsoTiempo_sol2[i])+" "+str(Nlista2[i])+" "+"\n")
archivo.close()