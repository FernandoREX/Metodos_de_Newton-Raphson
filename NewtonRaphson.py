# Métodos de Newton-Raphson

def NewthonRaphson (X0, tol, f, Df):
    ErrorMax=tol+1
    itemMax=500
    i=0
    Vx=[]

    while (ErrorMax>tol and i<=itemMax ): 
        i=i+1
        X1=X0-f(X0)/Df(X0)
        ErrorMax=abs(X1-X0)
        print("#{i:^2.0f}   X0={X0:^0.4f}    X1={X1:^0.4f}    ErrorMax={ErrorMax:^0.4f}".format(i=i,X0=X0,X1=X1,ErrorMax=ErrorMax))
        X0=X1
        Vx.append(X1)

    return i, X1, ErrorMax, Vx

def graficarError(Y):
    import matplotlib.pyplot as plt         #Instalar matplotlib con el comando < python -m pip install matplotlib > ó < py -m pip install matplotlib >
    fig, ax = plt.subplots()                #Esta funcion se encarga de graficar
    ax.plot(Y)
    ax.set(
        xlabel= "i",
        ylabel="X1",
        title="Newthon Raphson")
    ax.grid()
    plt.show()

from numpy import cos, sin, exp             #Instalar numpy con el comando < python -m pip install numpy > ó < py -m pip install numpy >
import numpy as np

f=lambda x: x          #Funcion del problema
Df=lambda x: 1         #Derivada de la funcion

X0=2        #Punto de inicio
tol=0.001   #Tolerancia


[i, X1, ErrorMax, Vx] = NewthonRaphson(X0, tol,f,Df)
print("\n------------------Conclusion-------------------------\n")
print("Newthon Raphson")
print("solucion de f(x)=4x-cos(x)")
print("iteraciones = ",i)
print("X1 = ",X1)
print("Error Maximo = ",ErrorMax)


graficarError (Vx)