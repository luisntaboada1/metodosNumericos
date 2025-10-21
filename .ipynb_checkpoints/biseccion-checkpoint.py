"""
Nieto Taboada Luis Antonio - 20204630806
3AM1
Metodos Numericos - Biseccion
"""
#Funciones
def f(x):
    return x - 100 # Expresion matematica.

def signo(a):
    if a == 0:
        return "0"
    elif a < 0:
        return "-"
    else: 
        return "+"


# valorX = [ limite, valor en f, signo ]
rangeHistory = list()
i = int(0)
maxIter = int(input('maximo numero de iteraciones: '))
stopDelta = ...
valoresInf = [0,0,0]
valoresSup = [0,0,0]
nuevoLim   = [0,0,0]


# Init
valoresInf[0] = float(input("Limite inferior (a): "))
valoresInf[1] = f(valoresInf[0])
valoresInf[2] = signo(valoresInf[1])

valoresSup[0] = float(input("Limite superior (b): "))
valoresSup[1] = f(valoresSup[0])
valoresSup[2] = signo(valoresSup[1])

rangeHistory.append([valoresInf[0], valoresSup[0]])


if valoresInf[2] == valoresSup[2]:
    print("escoja un rango cuyos limites tengan signo diferente en f. f(a)*f(b))<0. ")
else:
    while i < maxIter:
        print('\n')
        print(f'rango: [{valoresInf[0]}, {valoresSup[0]}]')
        print(f'valoresInf: {valoresInf}')
        print(f'valoresSup: {valoresSup}')        
        i = i + 1
        nuevoLim[0] = (valoresInf[0] + valoresSup[0]) / 2
        nuevoLim[1] = f(nuevoLim[0])
        nuevoLim[2] = signo(nuevoLim[1])
        print(f'nuevoLim: {nuevoLim}')

        if nuevoLim[2] == valoresInf[2]:
            valoresInf = nuevoLim
            print('inf')
        
        elif nuevoLim[2] == valoresSup[2]:
            valoresSup = nuevoLim
            print('sup')

        else: 
            print(f'raiz encontrada en: {nuevoLim}')
            rangeHistory.append([valoresInf[0], valoresSup[0]])
            break

        rangeHistory.append([valoresInf[0], valoresSup[0]])
        #nuevoLim = [0,0,0]

print(rangeHistory)