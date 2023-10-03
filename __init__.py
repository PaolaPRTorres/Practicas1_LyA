# Strings
nombre = "paola"
letra = nombre

print(letra)

for letra in nombre:
    print(letra)

texto = "En la fuente habia un chorrito"
if "chorrito" in texto:
    print("chorrito")


# Del sig Texto
# "Son las 7 de la noche y ya me quiero ir"
# Si Encuentra el Numero 7 y es menor a 8
# imprimir el numero 7 convertidp a INT
# y el texto, "Es hora de irnos son las : 7"

texto = "Son las 7 de la noche y ya me quiero ir"
if "7" in texto:
    num = 7
    if num<8:
        print("Es hora de irnos son las " + str(num))

## Slicing String
b = "Hola Mundo"
c = b[5:10]
print(c)
# Slicing por rango
print(b[5:9])
# Slicing desde el Inicio
print(b[:5])
# Slicing desde una posicion
print(b[5:])
# Slicing desde una posicion negativa
print(b[-5:-1])

## Boleanos
# Mayor que
print(10>9)
# Igual que
print(10==9)
# Menor que
print(10<9)

# variables boleanas
enStock = True
isTiendaAbierta = True

if enStock and isTiendaAbierta:
    print("VENDER PRODUCTOS")

tieneEfectivo = False
tieneTarjeta = True
if tieneTarjeta or tieneEfectivo:
    print("PAGO ACEPTADO")


regresateConfEx = False
if not regresateConfEx:
    print("MENTIROSO!")

paseLenguajes = False
if not paseLenguajes:
    print("FALSO")

isUpload = True
if not isUpload:
    print("REINTENTAR")


# operadores aritmeticos
x = 10
y = 5

# suma
print(x + y)

# Resta
print(x - y)

# Multiplicacion
print(x * y)

# Division
print(x / y)

# Modulo
print(x % y)

# Exponentes
print(2 ** 2)
print(x ** 2)
print(x ** y)

# floor division
print(4 // 2)
print(x // y)


# Operadores de asignacion
x = 30
x += 32
x -= 2
x *= 2
x /= 2
print(x)

# Operadores logicos de comparacion
a = 3
b = 2

# Igual
print(a == b)
# Diferente
print(a != b)
# Mayor
print(a > b)
# Menor
print(a < b)
# Mayor igual
print(a >= b)
# Menor igual
print(a <= b)


# Operadores Logicos

promedio = 100
asistencias = True
aprobado = (promedio > 70 ) and asistencias
# and, or, not
print(aprobado)


# Operadores de identidad

j = "HOLA"
k = "HOLA"
print(j is k.replace("",""))
print(j is not k)

# Operadores de pertenencia

print("A" in "HOLA")
print("A" not in "HOLA")

# Lista

frutas = ["Manzana","Banana", "Mango"]
frutas2 = ["🍎", "🍌", "🥭"]
print(frutas)
print(frutas2)
lista = [1,2,3,4,5,6]
logico = [True, False, True]
lista1 = ["abc", 34, True,'a', "🍎" ]
print(type(lista1))
print(lista1)

# List, Tuple, Set, Dictionary

"""
List: es una coleccion la cual esta ordenada
y muteable, la cual permite duplicados
"""
"""
Tuple: Es una coleccion la cual esta ordenada y no es un
modificable. Permite duplicados

Set: Es una coleccion la cual NO esta ordenada y no es un
modificable ni Indexada. NO permite duplicados 

Diccionario: Es una coleccion la cual esta ordenada
es modificable. No permite duplicados

"""
# Lista

lista1 = ("🐥", "🐵", "🐷")
lista1.index(1,"🐶")
lista1[2] = "🐯"
print(lista1)

# Tupla

tupla1 = ("🐥", "🐵", "🐷")
print(tupla1)

# Set

set1 = ("🐥", "🐵", "🐷")

# Diccionario
diccionario1 = {
    "pollo": "🐥",
    "monito": "🐵",
    "cerdito": "🐷"
}

diccionario1["koala"] = "🐨"
diccionario1["tigre"] = "🐯"
print(diccionario1["monito"])
print(diccionario1)

iturralde = diccionario1["pollo"]

print(iturralde)

# 0.- Crear una lista : 1, 2, 5, 3, 2, 3, 3, 6, 10, 8,
# 1.- Convertir la lista en un set para eliminar duplicados
# 2.- Calcular la suma de los numeros usando una lista
# 3.- Calcular la suma de los numeros usando un Set
# 4.- Crear un diccionario para almacenar las estadisticas, numeros unicos, suma total lista
#    y suma total Set Maximo valor, minimo valor Imprimir las estadisticas

ListaNumero = [1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9]
print("0.- Lista de Numeros:", ListaNumero)

ListaNumeroSet = set(ListaNumero)
print("1.- Lista sin Duplicados:", ListaNumeroSet)

SumaListaNumeros = sum(ListaNumero)
print("2.- Suma de los Numeros en Lista:", SumaListaNumeros)

SumaListaNumeroSet = sum(ListaNumeroSet)
print("3.- Suma de los Numeros en Lista:", SumaListaNumeroSet)

DiccionarioListas = {
    "len": len(ListaNumeroSet),
    "sumlista": SumaListaNumeros,
    "sumaset": SumaListaNumeroSet,
    "max": max(ListaNumero),
    "min": min(ListaNumero),
}

print("Diccionario:", DiccionarioListas)

# Condiciones
a= 200
b= 33

if b < a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")

# Ciclo while

quiereVolver = True
vecesRegresaron = 1
while vecesRegresaron <= 3:
    vecesRegresaron += 1
    print(f"Han vuelto {str(vecesRegresaron)} veces")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# ciclo for - for each
furtas = ["🍎", "🍌", "🥭"]

# for - Por cada
# for frutas in frutas:
    # print(frutas)
buscar = True
if buscar:
    for fruta in furtas:
        if fruta == "🍌":
            print("Se encontro:" + fruta)
    else:
        print("No Coincide")


print("INGRESA TU NOMBRE")
nombre = input()
print(type(nombre))
palabras = nombre.split(" ")
nombre = nombre.capitalize()
#nombre = nombre.replace(_old: " ", _new: " -")
b = ""             #variable

for palabra in palabras:      #ciclo
    b+= palabra.capitalize()+ " "

print(b)


# FUNCIONES CON PARAMETROS FINITOS
x = 1
def saludar(nombre, edad):
    print("Hola " + nombre + " EDAD: " + str(edad))

saludar(edad = 20, nombre="Juan")
saludar(nombre="Mateo", edad=21)
saludar("Alicia",24)

# FUNCIONES CON N PARAMETROS
def asistencia(*alumnos):
    print(alumnos[0])

asistencia("Ledead", "Laura", "Gustom")
asistencia("Iturraldead", "LeVoid")
asistencia("CJ")