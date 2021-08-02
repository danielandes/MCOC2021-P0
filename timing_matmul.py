from numpy import zeros
from time import perf_counter
N=1000
A=zeros((N,N))+1
B=zeros((N,N))+2
t1=perf_counter()
C=A@B
t2=perf_counter()
t=t2-t1
print("dt=",t)