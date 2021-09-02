from scipy.linalg import inv, solve
from numpy import double, ones
from time import perf_counter#from laplaciana import laplaciana
import scipy.sparse as sparse
import scipy.sparse.linalg as lin
from laplaciana import laplaciana, laplaciana_dispersa
N=[2,5,10,20,40,50,80,100,150,200,300,500,1000,2000,3000,4000,5000] #,2000,5000,10000


UsoTiempo_ens=[]
UsoTiempo_sol=[]
Nlista=[]
for a in range(10):
    for i in N:

        t1=perf_counter()
        A=laplaciana(i, double)
        t2=perf_counter()
        Am1=inv(A, overwrite_a=True)
        t3=perf_counter()
        t_ensamblaje=t2-t1
        t_solucion=t3-t2
        UsoTiempo_ens.append(t_ensamblaje)
        UsoTiempo_sol.append(t_solucion)
        Nlista.append(i)
        print(len(A))



#Creacion del archivo para guardar datos
archivo= open("inv_llena.txt", "w+")
for i in range(len(N*10)):
    archivo.write(str(UsoTiempo_ens[i])+" "+str(UsoTiempo_sol[i])+" "+str(Nlista[i])+" "+"\n")
archivo.close()
N2=[2,5,10,20,40,50,80,100,150,200,300,500,1000,2000,3000,4000,5000,6000]
UsoTiempo_ens2=[]
UsoTiempo_sol2=[]
Nlista2=[]
for a in range(10):
    for i in N2:

        t1=perf_counter()
        A=laplaciana_dispersa(i, double)
        A=sparse.csc_matrix(A)
        t2=perf_counter()
        Am1=lin.inv(A)
        t3=perf_counter()
        t_ensamblaje=t2-t1
        t_solucion=t3-t2
        UsoTiempo_ens2.append(t_ensamblaje)
        UsoTiempo_sol2.append(t_solucion)
        Nlista2.append(i)



#Creacion del archivo para guardar datos
archivo= open("inv_dispersa.txt", "w+")
for i in range(len(N2*10)):
    archivo.write(str(UsoTiempo_ens2[i])+" "+str(UsoTiempo_sol2[i])+" "+str(Nlista2[i])+" "+"\n")
archivo.close()