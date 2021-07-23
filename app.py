"""
nombre = input("ingrese un nombre:")
edad = float(input("edad:"))

i = 0
while i < 10:
    i = i +1
    if i%2!=0:
        print(i)

for i in range(1,10):
    if i%2!=0:
        print(i)

tupla = (20,True,"Carlos")
print(tupla[2])

lista1 = [23,568,90]
lista =[]
lista.append("Luis")
lista.append("CARLOS")
lista.append(23)
lista.append(False)
lista.append(lista1)
lista[1]=24
lista.pop(2)
for i in range(len(lista)):
    print(lista[i])
lista.clear()
print(len(lista))

dic = {
         "poo": 35,
          True: "Carlos",
          23:"Hola"
      }
dic[True]= 200
print(dic[True])
"""
from procesos.operaciones import *
def inicio():
    print("Examen complexivo")
    n = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))
    r = suma(n,n2)
    print("Total:",r)

def ejemplo1():
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    examen = float(input("Examen:"))
    r = getPromedio(nota1,nota2,examen)
    print("Promedio final:",r)
#inicio()
ejemplo1()

print("Prueba 2 23 de julio 2021")


print("Nelio")


