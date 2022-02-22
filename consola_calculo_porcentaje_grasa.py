# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:41:48 2022

@author: adria
"""
#==============================================================================
# MODULO INTERACCION CON EL USUARIO - 5
#==============================================================================


import calculadora_indices as calc 

def ejecutar_calcular_porcentaje_grasa() -> None:
    
    peso = float(input("Ingrese el peso de la persona (en Kg): "))
     
    altura = float(input("Ingrese la altura de la persona (en mt): "))
     
    edad = int(input("Ingrese la edad de la persona (en años): "))
    
    valor_genero = float(input("Ingrese el valor '10.8' en caso de ser hombre y, '0', en caso de ser mujer: "))
    
    
    print("\n%GC:",str(round(calc.calcular_porcentaje_grasa(peso,altura,edad,valor_genero),2))+"%")
    

def iniciar_aplicacion2() -> None:
    
    print("En esta funcion se va a calcular el Porcentaje De Grasa corporal (%GC)")
    
    ejecutar_calcular_porcentaje_grasa()

iniciar_aplicacion2()
