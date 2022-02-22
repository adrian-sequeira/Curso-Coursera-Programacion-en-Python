# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:01:15 2022

@author: adria
"""

#==============================================================================
# MODULO INTERACCION CON EL USUARIO - 1
#==============================================================================


import calculadora_indices as calc 

def ejecutar_calcular_calorias_en_actividad() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en Kg): "))
     
    altura = float(input("Ingrese la altura de la persona (en cm): "))
     
    edad = int(input("Ingrese la edad de la persona (en años): "))
    
    valor_genero = float(input("Ingrese el valor '5' en caso de ser hombre y, '-161', en caso de ser mujer: "))
    
    valor_actividad = float(input("Ingrese el valor que corresponde de acuerdo a lo sgte:\n'1.2' (POCO O NINGUN EJERCICIO)\n'1.375' (EJERCICIO LIGERO-1 a 3 días a la semana)\n'1.55' (EJERCICIO MODERADO-3 a 5 días a la semana)\n'1.72'(DEPORTISTA- 6 a 7 días a la semana)\n'1.9'(ATLETA)- entrenamientos mañana y tarde)\n: ")) 
 
    print("\nTMBactividadfisica:",round(calc.calcular_calorias_en_actividad(peso,altura,edad,valor_genero,valor_actividad),2),"cal")

def iniciar_aplicacion4() -> None:
    
    print("En esta funcion se va a calcular la Tasa Metabólica Basal según Actividad Fisica (TMBactividadfisica)")
    
    ejecutar_calcular_calorias_en_actividad()

iniciar_aplicacion4()
