from random import random, shuffle
import pandas as pd
import numpy as np

'''
2) Implementar un juego donde constas de 2 jarras, de capacidad 5 y 3 litros respectivamente, y debes colocar 4 litros en la jarra de 5L.
Las opciones posibles son:
* Llenar la jarra de 3 litros
* Llenar la jarra de 5 litros
* Vaciar la jarra de 3 litros
* Vaciar la jarra de 5 litros
* Verter el contenido de la jarra de 3 litros en la de 5 litros
* Verter el contenido de la jarra de 5 litros en la de 3 litros
'''

espacio_lleno = '|***|'
espacio_vacio = '|   |'

# 1. Crear las jarras analíticamente (Crear la clase)
class Jarra: 
    def __init__(self,capacidad:int):   # Parámetro
        # Propiedades del objeto
        self.litros = []            # Atributo = representación visual de la cantidad de litros
        self.cantLitros = 0
        self.capacidad = capacidad
    
        for i in range(capacidad):  # Modificador de un atributo -> litros 
            self.litros.append('|   |')

    # Acciones que se pueden aplicar a las propiedade del objeto 
    def visualizar(self):       # Método de la clase para visualizar 
        for i in self.litros: 
            print(i)
        print('TTTTT\n')

    def vaciar(self):           # Método de la clase para vaciar la jarra 
        for i in range(self.capacidad):
            self.litros.pop()
        for i in range(self.capacidad):
            self.litros.append('|   |')
        self.cantLitros = 0

    def llenar(self):           # Método de la clase para llenar la jarra 
        for i in range(self.capacidad):
            self.litros.pop()
        for i in range(self.capacidad):
            self.litros.append('|***|')
        self.cantLitros = self.capacidad

    def verter(self, otraJarra):           # Método de la clase para verter el contenido 
        DispOtraJarra = otraJarra.capacidad - otraJarra.cantLitros

        # Condiciones de verter
        if self.cantLitros > DispOtraJarra: 
            otraJarra.llenar()
            self.cantLitros -= DispOtraJarra
            for i in range(DispOtraJarra):
                self.litros.pop()
            for i in range(DispOtraJarra):
                self.litros.insert(0, '|   |')
        elif self.cantLitros <= DispOtraJarra: 
            otraJarra.cantLitros += self.cantLitros
            for i in range(self.cantLitros):
                otraJarra.litros.pop(0)
            for i in range(self.cantLitros):
                otraJarra.litros.append('|***|')
            self.vaciar()

# 1.1 Instanciamos el objeto 

Jarra5ltr = Jarra(5)
Jarra3ltr = Jarra(3)

# 2. Crear un menú
print("Menú:\n1. Llenar la jarra de 3 litros\n2. Llenar la jarra de 5 litros\n3. Vaciar la jarra de 3 litros\n4. Vaciar la jarra de 5 litros\n5. Verter el contenido de la jarra de 3 litros en la de 5 litros\n6. Verter el contenido de la jarra de 5 litros en la de 3 litros\n7. Salir")
opcion = int(input("Selecciona la acción que deseas hacer: "))
print("-----------------------------------------")

Contador = 0 
while opcion != 7:
    Contador += 1
    if opcion == 1: 
        Jarra3ltr.llenar()
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
        print("-----------------------------------------")
        print("Menú:\n1. Llenar la jarra de 3 litros\n2. Llenar la jarra de 5 litros\n3. Vaciar la jarra de 3 litros\n4. Vaciar la jarra de 5 litros\n5. Verter el contenido de la jarra de 3 litros en la de 5 litros\n6. Verter el contenido de la jarra de 5 litros en la de 3 litros\n7. Salir")
        print("-----------------------------------------")
    elif opcion == 2: 
        Jarra5ltr.llenar()
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
        print("-----------------------------------------")
        print("Menú:\n1. Llenar la jarra de 3 litros\n2. Llenar la jarra de 5 litros\n3. Vaciar la jarra de 3 litros\n4. Vaciar la jarra de 5 litros\n5. Verter el contenido de la jarra de 3 litros en la de 5 litros\n6. Verter el contenido de la jarra de 5 litros en la de 3 litros\n7. Salir")
        print("-----------------------------------------")
    elif opcion == 3: 
        Jarra3ltr.vaciar()
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
        print("-----------------------------------------")
        print("Menú:\n1. Llenar la jarra de 3 litros\n2. Llenar la jarra de 5 litros\n3. Vaciar la jarra de 3 litros\n4. Vaciar la jarra de 5 litros\n5. Verter el contenido de la jarra de 3 litros en la de 5 litros\n6. Verter el contenido de la jarra de 5 litros en la de 3 litros\n7. Salir")
        print("-----------------------------------------")
    elif opcion == 4: 
        Jarra5ltr.vaciar()
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
        print("-----------------------------------------")
        print("Menú:\n1. Llenar la jarra de 3 litros\n2. Llenar la jarra de 5 litros\n3. Vaciar la jarra de 3 litros\n4. Vaciar la jarra de 5 litros\n5. Verter el contenido de la jarra de 3 litros en la de 5 litros\n6. Verter el contenido de la jarra de 5 litros en la de 3 litros\n7. Salir")
        print("-----------------------------------------")
    elif opcion == 5: 
        Jarra3ltr.verter(otraJarra=Jarra5ltr)
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
        print("-----------------------------------------")
        print("Menú:\n1. Llenar la jarra de 3 litros\n2. Llenar la jarra de 5 litros\n3. Vaciar la jarra de 3 litros\n4. Vaciar la jarra de 5 litros\n5. Verter el contenido de la jarra de 3 litros en la de 5 litros\n6. Verter el contenido de la jarra de 5 litros en la de 3 litros\n7. Salir")
        print("-----------------------------------------")
    elif opcion == 6: 
        Jarra5ltr.verter(otraJarra=Jarra3ltr)
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
        print("-----------------------------------------")
        print("Menú:\n1. Llenar la jarra de 3 litros\n2. Llenar la jarra de 5 litros\n3. Vaciar la jarra de 3 litros\n4. Vaciar la jarra de 5 litros\n5. Verter el contenido de la jarra de 3 litros en la de 5 litros\n6. Verter el contenido de la jarra de 5 litros en la de 3 litros\n7. Salir")
        print("-----------------------------------------")
    if opcion > 7:
        print("-----------------------------------------")
        print("**** NO HAS SELECCIONADO UNA OPCIÓN VÁLIDA ****")
        print("-----------------------------------------")
        print("Menú:\n1. Llenar la jarra de 3 litros\n2. Llenar la jarra de 5 litros\n3. Vaciar la jarra de 3 litros\n4. Vaciar la jarra de 5 litros\n5. Verter el contenido de la jarra de 3 litros en la de 5 litros\n6. Verter el contenido de la jarra de 5 litros en la de 3 litros\n7. Salir")
        print("-----------------------------------------")
    # Si la jarra tiene 4 litros 
    opcion = int(input("Selecciona la acción que deseas hacer: "))
    print("-----------------------------------------")
    print("Tus intentos son: ", Contador)
print("!Fin del juego!❤️  Vuelve pronto")
print("-----------------------------------------")

# 3. Imprimir el resultado 







# Jarra de 5 litros con 2 de contenido 
# print('|  |\n|  |\n|  |\n|**|\n|**|\nTTTT')