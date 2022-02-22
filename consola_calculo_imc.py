# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:52:52 2022

@author: adria
"""
#==============================================================================
# MODULO INTERACCION CON EL USUARIO - 4
#==============================================================================



import calculadora_indices as calc 

def ejecutar_calcular_IMC() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en Kg): "))
     
    altura = float(input("Ingrese la altura de la persona (en mt): "))
     
    print("\nIMC:",round(calc.calcular_IMC(peso, altura),2))
    
def iniciar_aplicacion1() -> None:
    
    print("En esta funcion se va a calcular el Indice de Masa Corporal (IMC)")
    
    ejecutar_calcular_IMC()
     
iniciar_aplicacion1()     
