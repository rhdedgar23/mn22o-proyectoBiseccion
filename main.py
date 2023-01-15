# Metodos Numericos
# Trimestre 22-O
# Profesor Robin Preenja Sagar
# Proyecto Biseccion
# Por: Edgar Daniel Rodriguez Herrera

# Descripcion: El algoritmo pide un intervalo grande en donde hay que hallar todas
# las raices de la funcion sen().

import math

print("Por favor ingresa el intervalo en el que buscas raices para sen(x): ")
a = float(input("Cota inferior: "))
b = float(input("Cota superior: "))
errorBuscadoStr = input("Tolerancia (en notacion cientifica, p.e. 1e-6): ")
errorBuscadoFlt = float(errorBuscadoStr)


# definimos la funcion a usar
def f(x):
    return math.sin(x)


# definimos el metodo de biseccion
def biseccion(a, b, errorBuscado):
    # reasignamos variables para mejor entendimiento
    xizq = a
    xder = b

    # el ciclo while se detiene cuando hemos llegado al margen de error buscado
    while (abs(xizq - xder) >= errorBuscadoFlt):
        # evaluamos el punto medio
        c = (xizq + xder) / 2.0
        # y evaluamos el producto f(xizq)*f(c)
        prod = f(xizq) * f(c)

        # Si existen multiples raices o no existen raices en [xizq,c]
        if prod >= 0:
            # print("Multiples raices o no existen raices")
            # empezamos el metodo de biseccion en el intervalo [c, xder]
            xizq = c

        # Si existe una raiz en [xizq, c]
        elif prod <= 0:
            # empezamos el metodo de biseccion en el intervalo [xizq, c]
            xder = c

        else:
            print("Error!")
            quit()

    return c


# Creamos una lista para meter las raices
raices = []

# Primero, checamos si algun extremo del intervalo es una raiz.
if (f(a) == 0):
    raices.append(a)
elif (f(b) == 0):
    raices.append(b)

# luego, estimamos el numero de raices en el intervalo.
numRaices = (b // math.pi) - (a // math.pi)
# print("Numero de raices: ", numRaices, " + la raiz en 0.")

# Despues, dividimos el intervalo inicial en n=numRaices subintervalos y aplicamos
# el metodo de biseccion en cada uno de ellos.
numIntervalos = numRaices

anchoIntervalos = abs(a - b) / numIntervalos
# print("Ancho de intervalos: ", anchoIntervalos)

puntosDeIntervalos = [a]

for i in range(1, int(numIntervalos)):
    puntosDeIntervalos.append(a + (i * anchoIntervalos))

puntosDeIntervalos.append(b)
# print(puntosDeIntervalos)

for i in range(len(puntosDeIntervalos) - 1):
    # print(puntosDeIntervalos[i])
    # print(puntosDeIntervalos[i+1])
    raices.append(biseccion(puntosDeIntervalos[i], puntosDeIntervalos[i + 1], errorBuscadoFlt))

# Finalmente, imprimimos las raices
print("\nLas raices de la funcion sen(x) en el intervalo [", a, ", ", b, "] son:")
# print(errorBuscadoStr[-3])

# if(errorBuscadoStr[-3]=="-"):
#    print("2 digitos como exponente,", errorBuscadoStr[-2:])

# elif(errorBuscadoStr[-2]=="-"):
#    print("1 digito como exponente,", errorBuscadoStr[-1:])


for x in raices:
    if (errorBuscadoStr[-3] == "-"):
        errorPosDecimal = int(errorBuscadoStr[-2:])
        print(round(x, errorPosDecimal))
    elif (errorBuscadoStr[-2] == "-"):
        errorPosDecimal = int(errorBuscadoStr[-1:])
        print(round(x, errorPosDecimal))







