# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:50:04 2022

@author: adria
"""

#==============================================================================
# MODULO LOGICA PROYECTO - PROYECTO CALCULADORA INDICES CORPORALES
#==============================================================================

def calcular_IMC(peso: float, altura: float) -> float:
    
    '''Calcula el índice de masa corporal de una persona
    Parámetros:
        peso (float): Peso de la persona en kilogramos
        altura (float): Altura de la persona en metros
    Retorno:
        (float): Índice de masa corporal de la persona'''
        
    return peso/altura**2

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    
    '''Calcula el porcentaje de grasa de una persona
    Parámetros:
        peso (float): Peso de la persona en kilogramos
        altura (float): Altura de la persona en metros
        edad (int): Edad de la persona en años
        valor_genero (float): Valor que, en caso de ser masculino debe ser 10.8 y, en caso de ser femenino, debe ser 0
    Retorno:
        (float): Porcentaje de grasa que tiene el cuerpo de la persona''' 
        
    return 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero:int) -> float:
    
    '''Calcula tasa  metabólica  basal
    Parámetros:
        peso (float): Peso de la persona en kilogramos
        altura (float): Altura de la persona en centimetros
        edad (int): Edad de la persona en años
        valor_genero (int): Valor que, en caso de ser masculino debe ser 5 y,en caso de ser femenino, debe ser -161
    Retorno:
        (float):Cantidad de calorías que la persona quema en reposo'''
        
    return (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero 

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero:int, valor_actividad: float) -> float:
    
    '''Calcula tasa  metabólica  basal segun actividad fisica
    Parámetros:
        peso (float): Peso de la persona en kilogramos
        altura (float): Altura de la persona en centimetros
        edad (int): Edad de la persona en años
        valor_genero (int): Valor que, en caso de ser masculino debe ser 5 y,en caso de ser femenino, debe ser -161
        valor_actividad (float): Valor que depende de la actividad física semanal, 
                                    •  1.2: poco o ningún ejercicio 
                                    •  1.375: ejercicio ligero (1 a 3 días a la semana) 
                                    •  1.55: ejercicio moderado (3 a 5 días a la semana) 
                                    •  1.725: deportista (6-7 días a la semana) 
                                    •  1.9: atleta (entrenamientos mañana y tarde)
    Retorno:
        (float):Cantidad de calorías que la persona quema, al realizar algun tipo de actividad física semanalmente'''
    
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    
    return tmb * valor_actividad

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero:int) -> str:
    
    '''Calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar
    Parámetros:
        peso (float): Peso de la persona en kilogramos
        altura (float): Altura de la persona en centimetros
        edad (int): Edad de la persona en años
        valor_genero (int): Valor que, en caso de ser masculino debe ser 5 y,en caso de ser femenino, debe ser -161
    Retorno:
        (str): Una cadena indicando el rango de calorías que una persona debe consumir si desea adelgazar '''
        
    consumo_inferior = round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.80,2)
    consumo_superior = round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero) * 0.85,2)
    
    return print (" Para adelgazar es recomendado que consumas entre:", consumo_inferior, "y", consumo_superior, "calorías al día")