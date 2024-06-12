from math import *

#importamos esta libreria para dibujar la tabla en donde veremos las iteraciones

from tabulate import tabulate 


#esta funcion nos devuelve el resultado usando la funcion eval, la cual evalua x en una cadena de texto
def evaluarFunc(funcion,x):
        return eval(funcion)

#en esta funcion aplicamos el metodo biseccion para encontrar la raiz
def metodoBiseccion(funcion,a,b,tolerancia):
        #usamos una lista para almacenar los resultados de cada iteracion
        iteraciones=[]
        #contador
        iteracion=0
        #bucle hasta que cada iteracion sea menor a la tolerancia que introduzcamos
        while (b-a)/2>tolerancia:

                #evaluamos cada punto en la funcion
                x=a
                fa=evaluarFunc(funcion,x)
                x=b
                fb=evaluarFunc(funcion,x)
                #calculamos el punto medio
                m=(a+b)/2
                x=m
                fm=evaluarFunc(funcion,x)
                #calculamos el error
                error=(b-a)/2*100
                #guardamos los resultados en nuestra lista de iteraciones
                iteraciones.append([a,fa,b,fb,m,fm,error])

                #si al evaluar el punto medio llega a 0 se ha encontrado la raiz exacta
                if fm==0:
                        break
                #si f(m) tiene signo opuesto a f(a) se redefine como [a,m]
                elif fa*fm<0:
                        b=m
                #si f(m) tiene signo opuesto a f(b) se redefine como [m,b]
                else:
                        a=m
                iteracion+=1
        return iteraciones #devuelve el listado de todas las iteraciones

#funcion para solicitar los datos de entrada al usuariocd
def puntos():
        funcion=input("Ingrese la funcion: ")
        a=float(input("Ingrese el punto a: "))
        b=float(input("Ingrese el punto b: "))
        tolerancia=float(input("Ingrese la tolerancia: "))

        #llamamos al metodoBiseccion con sus parametros

        iteraciones = metodoBiseccion(funcion,a,b,tolerancia)



        #encabezados de la tabla
        headers = ["iteracion","a", "f(a)", "b", "f(b)", "mi", "f(mi)","Error"]
        table = [[i]+iteracion for i, iteracion in enumerate (iteraciones)]
    
        #se imprime la tabla con los resultados
        print(tabulate(table, headers=headers, tablefmt="grid"))

#se llama a la funcion para ejecutar el programa
puntos()
