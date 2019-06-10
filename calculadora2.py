#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Usuario
#
# Created:     07/02/2019
# Copyright:   (c) Usuario 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#importaciones

from tkinter import *
import tkinter
from tkinter import messagebox
import math

#constanmtes

posininumerosx=100
posininumerosy=100
fuente=13
numeros=["7","8","9","4","5","6","1","2","3","0"]
texto=""
tx=""

cuenta=[]
operacion=[]
operaciones=["/","*","-","+","="]
cuen=False
correcto=False

#funciones
def detectar(elem):
    global numeros
    global operaciones
    global correcto
    global tx

    for ele in numeros:

        if elem==ele:

            correcto=True
            tx=str(tx)
            tx+=elem

    for el in operaciones:

        if elem==el:
            correcto=True

def fnKeyPress(key):
    global correcto
    global texto
    global tx
    global cuen

    text= key.char
    detectar(str(text))

    if correcto== True:

        texto+=text

    elif correcto==False:
        entrada.set(texto)

    correcto=False



def borrar():

    global tx
    global texto

    del cuenta[:]
    del operacion[:]
    tx=""
    texto=""
    entrada.set(texto)


def detectar_numeros(cadena):
    global cuenta
    global operacion
    global numeros
    global correcto

    tx=""
    v=0
    print(cadena)
    for elem in cadena:

        for ele in numeros:

            if elem==ele:
                correcto=True

        if correcto==True:

            if detec_operacion(elem) == False:

                tx += elem

            else:

                operacion.append(elem)

                if detec_decimal(tx)==True:

                    cuenta.append(float(tx))

                else:

                    cuenta.append(int(tx))

                tx=""
        v+=1

    correcto=False


def detec_operacion(num):
    global operaciones

    for elem in operaciones:
        if num==elem:
            return True

    return False

def detec_decimal(num):

    for elem in num:

        if elem==".":

            return True

    return False


def calcular():
    global cuenta
    global operacion

    negativo=False

    resul = 0
    v=1

    texto=entrada.get()

    if texto[0]=="-":

        negativo=True

    for i in range (len(cuenta)):

        if v==1:
            a=cuenta[i]

        elif v==2:

            b=cuenta[i]

            if operacion[i-1]=="/":

                if not b == 0:

                    if negativo==False:
                        resul=a/b
                    else:
                        resul=-a/b
                else:
                    resul=0
                    messagebox.showerror(message="No se puede dividir por cero"
                    , title="Error")
                    resul=0

            elif operacion[i-1]=="*":

                if negativo==False:
                    resul=a*b
                else:
                    resul=-a*b

            elif operacion[i-1]=="-":

                if negativo==False:
                    resul=a-b
                else:
                    resul=-a-b

            elif operacion[i-1]=="+":

                if negativo==False:
                    resul=a+b
                else:
                    resul=-a+b


            a=resul
            v=1

        v+=1

    return resul


def ingresar(num):
    global cuen
    global texto
    global tx

    if detec_operacion(num):

        cuen=False

        tx=""
        texto += str(num)

        if num== "=":

            if len(texto)>0:

                entrada.set(texto)

            detectar_numeros(entrada.get())

            cuen=True

            opera=calcular()
            print(opera)
            del cuenta[:]
            del operacion[:]


    elif not detec_operacion(num):

        if cuen==True:
            texto=""
            tx=""
            cuen=False

        if (detec_decimal(str(num))==True):

            if len(tx)==0:
                tx="0."
                texto += "0."
        else:
            tx += str(num)

            texto += str(num)

    if (num=="="):

        texto=str(opera)
        tx=opera

    entrada.set(texto)


def botones(X,Y,txt):

    global fuente
    tamano=2

    if (txt=="0"):
        tamano=5
        Y+=2

        btn0=Button(ventana,text=txt,
        command=lambda:ingresar(int(txt)),
        font=("Arial",13),width=tamano).place(x=X,y=Y)

    elif (detec_operacion(str(txt))==True):

        if (txt=="+"):

            btndec=Button(ventana,text=txt,
            command=lambda:ingresar(str(txt)),
            font=("Arial",13),width=tamano,height=4).place(x=X,y=Y)

        elif (txt=="="):

            btndec=Button(ventana,text=txt,
            command=lambda:ingresar(str(txt)),
            font=("Arial",13),width=tamano,height=3).place(x=X,y=Y)

        else:

            btndec=Button(ventana,text=txt,
            command=lambda:ingresar(str(txt)),
            font=("Arial",13),width=tamano).place(x=X,y=Y)

    elif (detec_decimal(str(txt))==True):

            btndec=Button(ventana,text=txt,
            command=lambda:ingresar(str(txt)),
            font=("Arial",13),width=tamano).place(x=X,y=Y)

    else:

        btn=Button(ventana,text=txt,
        command=lambda:ingresar(int(txt)),
        font=("Arial",13),width=tamano).place(x=X,y=Y)

def crear_matriz(n,rango):

    lista=[n]

    for i in range (rango):

        n+=30
        lista.append(n)

    return lista


def crear_botones(lx,ly):

    global numeros

    n=0

    for j in range (len(ly)):

        for i in range (len(lx)):
            botones(lx[i],ly[j],numeros[n])

            if n<len(numeros)-1:
                n+=1

def bt_operaciones(lx,ly):

    global operaciones

    for i in range (len(lx)):
            botones(lx[i],ly[0]-30,operaciones[i])

ventana=tkinter.Tk()

ventana.geometry("500x300")

ventana.title("Calculadora 0.01")

etiqueta = Label(text="Super Calculadora 2001",font=("", 20),
fg="blue",background="white").place(x=50,y=5)

entrada=StringVar()

entrada.set("")

txtProducto=Entry(ventana,textvariable=entrada).place(x=80,y=40)

#matriz

matrizx=crear_matriz(posininumerosx,2)

matrizy=crear_matriz(posininumerosy,2)

crear_botones(matrizx,matrizy)

bcero= botones(matrizx[0]+2,matrizy[2]+30,"0")

bdecim= botones(matrizx[2],matrizy[2]+32,".")

bt_operaciones(matrizx,matrizy)

bmas= botones(matrizx[2]+30,matrizy[0]-30,"+")

bigual= botones(matrizx[2]+30,matrizy[2],"=")

bC= Button(ventana,text="C",
    command=borrar,
    font=("Arial",13),width=2).place(x=matrizx[2]+60,y=matrizy[2]+30)

ventana.bind("<Key>", fnKeyPress)


ventana.mainloop()


