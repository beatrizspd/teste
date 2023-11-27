
import matplotlib.pyplot as plt
import math

def f(x):
    return 0.5*(x-2)**2
def df(x):
    return x-2  
intervalo=([-0.7,2.6],[0.4,1.7])
e=10**-5

#Exercicio 3.A
def num_ouro(a,b):
    phi=(1+math.sqrt(5))/2
    x0=b-((b-a)/phi)
    x1=a+((b-a)/phi)
    while (abs(b-a))/(abs(x0+x1))>e:
        if (f(x0))<(f(x1)):
            b=x1
        else:
            a=x0
        x0=b-((b-a)/phi)
        x1=a+((b-a)/phi)
    return (b+a)/2
for a in intervalo:
    print(num_ouro(a[0],a[1]))

#Exercicio 3.B
def gradiente(x0,e,lambd,kmax):
    d=df(x0)
    x1=x0-lambd*d
    k=0
    xaxis=[]
    yaxis=[]
    n=0
    while abs(lambd*d)>e and k<kmax:
        x0=x1
        d=df(x0)
        x1=x0-lambd*d
        k=k+1
        n+=1
        xaxis.append(n)
        yaxis.append(x1)
    return x1,xaxis,yaxis
for l in (0.1, 0.5, 1, 2, 2.1):
    print(gradiente(0,e,l,10)[0])


#Exercicio 3.C

for l in (0.1, 0.5, 1, 2, 2.1):
    plt.plot(gradiente(0,e,l,10)[1],gradiente(0,e,l,10)[2],'.-',label = l)
plt.xlabel("Numero Iteracoes")
plt.ylabel("Valor do minimo")
plt.title('Valores do minimo para cada lambda em funcao do numero de iteracoes')
plt.legend(loc='upper left',fontsize=8)
plt.grid()
plt.show()

    