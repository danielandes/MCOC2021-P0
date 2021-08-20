import matplotlib.pylab as plt
#Recuperacion de datos desde el archivo


Nombres= ["B_I_d.txt","B_II_F_d.txt","B_II_T_d.txt","B_III_F_d.txt","B_III_T_d.txt","B_IV_F_d.txt","B_IV_T_d.txt","B_V_F_d.txt","B_V_T_d.txt"]
Tiempolimpio=[]
Nlimpio=[]
for nombre in Nombres:
    Tiempotxt=[]
    Ntxt=[]
    lectura= open(nombre, "r")
    for i in lectura:
        
        valores=i.split(" ")
        valores.pop()
        Tiempotxt.append(float(valores[0]))
        Ntxt.append(float(valores[1]))
    lectura.close()
    a=len(Ntxt)/10
    a=int(a)
    for i in range(a):
        suma=0
        suma2=0
        for j in range(10):
            suma+=Tiempotxt[i+a*j]
            suma2+=Ntxt[i+a*j]
        Tiempolimpio.append(suma/10)
        Nlimpio.append(suma2/10)
     
        
a=int(len(Tiempolimpio)/len(Nombres))

#Graficar
xlabels= ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
xN=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
ytiempolabels= ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
ytiempoT=[(10**-4),(10**-3),(10**-2),(10**-1),(1),(10),(60),(600)]
ymemorialabels= ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
ymemoriaB= [(10**3),(10**4),(10**5),(10**6),(10**7),(10**8),(10**9),(10**10)]


plt.figure(1)
plt.subplot(1,1,1)
plt.title("Casos B double")
for i in range(len(Nombres)):
    plt.loglog(Nlimpio[a*i:a*i+a],Tiempolimpio[a*i:a*i+a], marker="o")
plt.xticks(xN,xlabels, rotation=60)
plt.grid(True)
plt.yticks(ytiempoT,ytiempolabels)
plt.legend(Nombres)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamano matriz N")
plt.show()


Nombres2= ["B_I_f.txt","B_II_F_f.txt","B_II_T_f.txt","B_III_F_f.txt","B_III_T_f.txt","B_IV_F_f.txt","B_IV_T_f.txt","B_V_F_f.txt","B_V_T_f.txt"]
Tiempolimpio2=[]
Nlimpio2=[]
for nombre in Nombres2:
    Tiempotxt2=[]
    Ntxt2=[]
    lectura2= open(nombre, "r")
    for i in lectura2:
        
        valores=i.split(" ")
        valores.pop()
        Tiempotxt2.append(float(valores[0]))
        Ntxt2.append(float(valores[1]))
    lectura.close()
    a=len(Ntxt2)/10
    a=int(a)
    for i in range(a):
        suma=0
        suma2=0
        for j in range(10):
            suma+=Tiempotxt2[i+a*j]
            suma2+=Ntxt2[i+a*j]
        Tiempolimpio2.append(suma/10)
        Nlimpio2.append(suma2/10)
  
        
a=int(len(Tiempolimpio2)/len(Nombres2))

#Graficar
xlabels= ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
xN=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
ytiempolabels= ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
ytiempoT=[(10**-4),(10**-3),(10**-2),(10**-1),(1),(10),(60),(600)]
ymemorialabels= ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
ymemoriaB= [(10**3),(10**4),(10**5),(10**6),(10**7),(10**8),(10**9),(10**10)]


plt.figure(1)
plt.subplot(1,1,1)
plt.title("Casos B float")
for i in range(len(Nombres2)):
    plt.loglog(Nlimpio2[a*i:a*i+a],Tiempolimpio2[a*i:a*i+a], marker="o")
plt.xticks(xN,xlabels, rotation=60)
plt.grid(True)
plt.yticks(ytiempoT,ytiempolabels)
plt.legend(Nombres2)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamano matriz N")
plt.show()

for i in range(len(Nombres)):
    plt.figure(1)
    plt.subplot(1,1,1)
    plt.title("double / float")
    plt.loglog(Nlimpio[a*i:a*i+a],Tiempolimpio[a*i:a*i+a], marker="o")
    plt.loglog(Nlimpio2[a*i:a*i+a],Tiempolimpio2[a*i:a*i+a], marker="o")
    plt.xticks(xN,xlabels, rotation=60)
    plt.grid(True)
    plt.yticks(ytiempoT,ytiempolabels)
    paralegend=[]
    paralegend.append(Nombres[i])
    paralegend.append(Nombres2[i])
    plt.legend(paralegend)
    plt.ylabel("Tiempo transcurrido")
    plt.xlabel("Tamano matriz N")
    plt.show()