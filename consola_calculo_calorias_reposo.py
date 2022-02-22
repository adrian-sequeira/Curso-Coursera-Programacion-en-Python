# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:55:40 2022

@author: adria
"""

#==============================================================================
# MODULO INTERACCION CON EL USUARIO - 3
#==============================================================================


import calculadora_indices as calc 

def ejecutar_calcular_calorias_en_reposo() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en Kg): "))
     
    altura = float(input("Ingrese la altura de la persona (en cm): "))
     
    edad = int(input("Ingrese la edad de la persona (en años): "))
    
    valor_genero = float(input("Ingrese el valor '5' en caso de ser hombre y, '-161', en caso de ser mujer: "))
    
    
    print("\n%TMB:",round(calc.calcular_calorias_en_reposo(peso,altura,edad,valor_genero),2),"cal")
    

def iniciar_aplicacion3() -> None:
    
    print("En esta funcion se va a calcular la Tasa Metabólica Basal (TMB)")
    
    ejecutar_calcular_calorias_en_reposo()

iniciar_aplicacion3()
