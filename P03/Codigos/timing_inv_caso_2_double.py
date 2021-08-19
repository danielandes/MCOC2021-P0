from scipy import double
from time import perf_counter
import matplotlib.pylab as plt
from scipy.linalg import inv
from laplaciana import laplaciana
N=[2,5,10,20,40,50,70,100,400,800,1500,2000,2500,5000,6000]
UsoMemoria=[]
UsoTiempo=[]
Nlista=[]
for a in range(10):
    for i in N:
        t1=perf_counter()
        A=laplaciana(i, double)
        t2=perf_counter()
        Am1=inv(A, overwrite_a=False)
        t3=perf_counter()
        t_ens=t2-t1
        t_inv=t3-t2
        UsoTiempo.append(t_inv)
        memoria=  A.nbytes+Am1.nbytes
        UsoMemoria.append(memoria)
        Nlista.append(i)
print(A.nbytes, Am1.nbytes)




#Creacion del archivo para guardar datos
archivo= open("recursos_inv_caso_2_double.txt", "w+")
for i in range(len(N*10)):
    archivo.write(str(UsoMemoria[i])+" "+str(UsoTiempo[i])+" "+str(Nlista[i])+" "+"\n")
archivo.close()