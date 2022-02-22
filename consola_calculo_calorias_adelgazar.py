58# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:30:39 2022

@author: adria
"""

#==============================================================================
# MODULO INTERACCION CON EL USUARIO - 2
#==============================================================================


import calculadora_indices as calc 

def ejecutar_consumo_calorias_recomendado_para_adelgazar() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en Kg): "))
     
    altura = float(input("Ingrese la altura de la persona (en cm): "))
     
    edad = int(input("Ingrese la edad de la persona (en años): "))
    
    valor_genero = float(input("Ingrese el valor '5' en caso de ser hombre y, '-161', en caso de ser mujer: "))
    
    
    calc.consumo_calorias_recomendado_para_adelgazar(peso,altura,edad,valor_genero)
    
def iniciar_aplicacion5() -> None:
    
    print("En esta funcion se va a calcular la cantidad de calorias recomendadas que una persona debe consumir a diario, en caso que desee adelgazar")
    
    ejecutar_consumo_calorias_recomendado_para_adelgazar()

iniciar_aplicacion5()
