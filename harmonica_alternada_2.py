# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 22:32:51 2011

@author: Claudio *8486
"""

from fractions import Fraction
from matplotlib.pyplot import plot

def serie_harmonica_alternada(inicial, sinal):
    denominador = inicial
    while denominador < float('inf'):
        yield Fraction(sinal*1, denominador)
        denominador += 2
        
def esta_proximo(o_alvo, dada_a_tolerancia, da_soma_parcial):
    if o_alvo == da_soma_parcial: return True
    return abs(da_soma_parcial - o_alvo) < dada_a_tolerancia
  
parciais = []
def aproxima(o_alvo, da_soma_parcial, com_parcelas):
    parciais.append(da_soma_parcial)
    da_soma_parcial += com_parcelas.next()
    if (abs(da_soma_parcial) - o_alvo) > 0: return da_soma_parcial
    return aproxima(o_alvo, da_soma_parcial, com_parcelas)
    
def converge(o_alvo, dada_a_tolerancia=0.1, da_soma_parcial=0):
    com_positivos = serie_harmonica_alternada(1, 1)
    com_negativos = serie_harmonica_alternada(2, -1)
    
    da_soma_parcial += aproxima(o_alvo, da_soma_parcial, com_positivos)
    if esta_proximo(o_alvo, dada_a_tolerancia, da_soma_parcial):
        return da_soma_parcial
        
    da_soma_parcial += aproxima(o_alvo, da_soma_parcial, com_negativos)
    if esta_proximo(o_alvo, dada_a_tolerancia, da_soma_parcial):
        return da_soma_parcial
        
    return converge(o_alvo, dada_a_tolerancia, da_soma_parcial)

def plotar(o_alvo, parciais=parciais):  
#    plot([limite-epsilon] * len(parciais))
    plot([o_alvo] * len(parciais))
#    plot([limite+epsilon] * len(parciais))
    plot(parciais)
    plot(parciais, 'o')       
