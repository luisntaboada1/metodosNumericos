"""
Nieto Taboada Luis Antonio - 20204630806
3AM1
Metodos Numericos - Biseccion
"""

def f(x):
    return x - 100 # Cambiar a cualquier ecuacion.

def signo(a):
    if a == 0:
        return "0"
    elif a < 0:
        return "-"
    else: 
        return "+"


i = int(0) 
rango = [0, 0]
rango[0] = float(input("limite inferior: ")) 
rango[1] = float(input("limite superior: "))
maxIter = int(input("numero maximo de iteraciones: "))

finf = f(rango[0])
signoinf = signo(finf)

fsup = f(rango[1])
signosup = signo(fsup)

print(f"0: {rango}")
while i < maxIter:
    i = i+1
    nlim = (rango[0] + rango[1]) / 2
    fnlim = f(nlim)
    nsigno = signo(fnlim)

    if nsigno == signoinf:
        rango[0] = nlim
        finf = fnlim
        signoinf = nsigno
    
    elif nsigno == signosup:
        rango[1] = nlim
        fsup = fnlim
        signosup = nsigno
    
    else: 
        rango = nlim
        print(f"se encontro la raiz en {rango}")
        break

    print(f"{i}: {rango}")


"""
A grandes rasgos, el algoritmo de biseccion consiste en: 
1. Establecer un rango inicial [a, b] en el cual se sabe que existe una raiz.
2. Calcular el punto medio del rango
2.1. Si el punto medio tiene el mismo signo que el limite inferior, se sustituye el limite inferior por el punto medio.
2.2. Si el punto medio tiene el mismo signo que el limite superior, se sustituye el limite superior por el punto medio.
Cuando se llegue a un delta lo suficientemente pequeño, se puede considerar que el punto medio es la raiz. En este caso, el delta es el de maquina.
"""