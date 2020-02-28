""" Lineas de código que demuestra que si dentro de un string se encuentra
un número entero, el método loads de la clase json lo convierte en un entero. """

from json import loads

entero = "1"
print(type(entero))
cadena = "Hola Mundo"
print(type(cadena))
diccionario = {"Hola":"Mundo"}
print(type(diccionario))
diccionario_cadena = "{'Hola':'Mundo'}"
print(type(diccionario_cadena))
lista = []
print(type(lista))

print(f'Entero: {type(loads(entero))}')
#print(f'Cadena: {type(loads(cadena))}')
#print(f'Diccionario: {type(loads(diccionario))}')
#print(f'Diccionario Cadena: {type(loads(diccionario_cadena))}')
#print(f'Lista: {type(loads(lista))}')
