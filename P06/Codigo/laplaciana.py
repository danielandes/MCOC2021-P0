import scipy.sparse as sparse
from numpy import zeros, eye
def laplaciana(N, a):
#    A = zeros((N,N), dtype=a)
#    for i in range(N):
#        A[i,i]=2
#        for j in range(i-1,i):
#            if abs(i-j)==1:
#                A[i,j]=-1
#                A[j,i]=-1
#        A[0,N-1]=0
#        A[N-1,0]=0
#    return(A)
    e=eye(N)-eye(N,N,1)
    return(a(e+e.T))
def laplaciana_dispersa(N, a):   
    e=sparse.eye(N, dtype=a)-sparse.eye(N,N,1, dtype=a)
    return(e+e.T)