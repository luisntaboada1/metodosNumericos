"""
Nieto Taboada Luis Antonio - 20204630806
3AM1
Metodos Numericos - Biseccion
"""

def f(x):
    return x - 100 

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
print(f"0: {rango}")

while i < maxIter:
    i = i+1
    nlim = (rango[0] + rango[1]) / 2
    finf = f(rango[0])
    fsup = f(rango[1])
    fnlim = f(nlim)
    print("--------------------------------------------------")
    print(f"nuevo limite: ({rango[0]} + {rango[1]}) / 2 = {nlim}")
    print(f"f({rango[0]}) = {finf}")
    print(f"f({rango[1]}) = {fsup}")
    print(f"f({nlim}) = {fnlim}")
    

    if signo(fnlim) == signo(finf):
        rango[0] = nlim
        print(f"{i}: {rango} : d={rango[1]-rango[0]}")

    elif signo(fnlim) == signo(fsup):
        rango[1] = nlim
        print(f"{i}: {rango} : d={rango[1]-rango[0]}")

    else:
        rango = [nlim]
        print(f"se encontro la raiz {rango}: f({rango}) = {fnlim}")
        print("\n")
        break
