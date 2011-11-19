# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 22:32:51 2011

@author: Claudio
"""

from fractions import Fraction
from matplotlib.pyplot import plot



def serie_harmonica_alternada(inicial, sinal):
    denominador = inicial
    while denominador < float('inf'):
        yield Fraction(sinal*1, denominador)
        denominador += 2
        
def converge(limite, epsilon=0.1):
    positivos = serie_harmonica_alternada(1, 1)
    negativos = serie_harmonica_alternada(2, -1)
    positiva_convergiu = False
    negativa_convergiu = False
    
    sequencia_alternada_de_parcelas = [1]
    
    p1 = positivos.next()
    soma_parcial = p1
    soma_ate_aqui = [p1]
    
    sinal_corrente = 1
    def manteve_sinal(parcela):
        return (parcela * sinal_corrente) > 0
        
    def plotar():  
        plot([limite-epsilon] * len(soma_ate_aqui))
        plot([limite] * len(soma_ate_aqui))
        plot([limite+epsilon] * len(soma_ate_aqui))
        plot(soma_ate_aqui)
        plot(soma_ate_aqui, 'o')
        
    while not ( soma_parcial == limite or
                abs(soma_parcial - limite) < epsilon
                    and positiva_convergiu
                    and negativa_convergiu
                ):
                
        while soma_parcial < limite:
            p = positivos.next()
            soma_parcial += p
            soma_ate_aqui.append(soma_parcial)

            if manteve_sinal(p):
                sequencia_alternada_de_parcelas[-1] += 1
            else:
                sequencia_alternada_de_parcelas.append(1)
                sinal_corrente = p
                
            if abs(soma_parcial - limite) < epsilon:
                positiva_convergiu = True
                break
        
        while soma_parcial > limite:
            if positiva_convergiu and negativa_convergiu:
                break

            p = negativos.next()
            soma_parcial += p
            soma_ate_aqui.append(soma_parcial)
            
            if manteve_sinal(p):
                sequencia_alternada_de_parcelas[-1] += 1
            else:
                sequencia_alternada_de_parcelas.append(1)
                sinal_corrente = p
                
            if abs(soma_parcial - limite) < epsilon:
                negativa_convergiu = True
                break

    plotar()
    return sequencia_alternada_de_parcelas
     