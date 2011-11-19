# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 22:32:51 2011

@author: Claudio Berrondo*
Mestradao em Modelagem Matematica da Informacao
para a disciplina Modelagem Matematica para Aplicacoes
do professor Antonio C. S. Branco

*obrigado a Debora, pelas ideias iniciais dos loops while, ao Diego pela ajuda nas 
exatas condicoes de parada para esses loops, ao Andre pela dica da implementacao 
em Lisp do SICP, ao Gerson, Ariel, Daniel, Pablo e Antoanne.
"""

"""
questao 2: A serie geometrica desta questao e uma serie absolutamente convergente. 
Neste caso, qualquer arranjo dos termos convergira sempre para o mesmo valor para
o qual a serie original converge. Sendo assim, nao e possivel uma implementacao 
semelhante.
"""

from fractions import Fraction
from matplotlib.pyplot import plot

def serie_harmonica_alternada(inicial, sinal):
    denominador = inicial
    while denominador < float('inf'):
        yield Fraction(sinal*1, denominador)
        denominador += 2
        
def eh_positivo(numero):
    return numero >= 0
         
def eh_negativo(numero):
    return numero < 0 
    
class Converge:
    def __init__(self, limite, epsilon=0.1):
        self.limite = limite
        self.epsilon = epsilon
        self.positivas = serie_harmonica_alternada(1, 1)
        self.negativas = serie_harmonica_alternada(2, -1)
        
        self.positiva_convergiu = False
        self.negativa_convergiu = False
        
        self.soma_parcial = 0
        self.soma_acumulada = []

        self.sinal_corrente = 1
        self.sequencia_alternada_de_parcelas = [0]
        
        # convencionou-se que a primeira parcela sera sempre 1/1:
        self.registrar(self.positivas.next())
        
    def manteve_sinal(self, parcela):
        return eh_positivo(parcela * self.sinal_corrente)
        
    @property
    def total_de_parcelas(self):
        return len(self.soma_acumulada)
        
    def registrar(self, parcela):
        self.soma_parcial += parcela
        self.soma_acumulada.append(self.soma_parcial)
        
        if self.manteve_sinal(parcela):
            self.sequencia_alternada_de_parcelas[-1] += 1
        else:
            self.sequencia_alternada_de_parcelas.append(1)
            self.sinal_corrente = parcela
            
    def convergiu(self, parcela):
        if self.parcelas_convergiram:   # ambas parcelas ok!
            return True

        self.registrar(parcela)
        
        if self.soma_convergiu:
            if eh_positivo(parcela):
                self.positiva_convergiu = True
                return True
                
            elif eh_negativo(parcela):
                self.negativa_convergiu = True
                return True

    @property            
    def distancia_para_o_limite(self):
        return abs(self.soma_parcial - self.limite)
        
    @property
    def o_limite_foi_atingido(self):
        return self.distancia_para_o_limite == 0
        
    @property
    def soma_convergiu(self):
        return self.distancia_para_o_limite < self.epsilon
        
    @property
    def parcelas_convergiram(self):
        return self.positiva_convergiu and self.negativa_convergiu
        
    @property
    def soma_e_parcelas_convergirem(self):
        if self.o_limite_foi_atingido:   # soma == limite
            return True
        return self.soma_convergiu and self.parcelas_convergiram
            
            
    def converge(self):
        while not self.soma_e_parcelas_convergirem:
            
            while self.soma_parcial < self.limite:
                if self.convergiu(self.positivas.next()):
                    break
                
            while self.soma_parcial > self.limite:
                if self.convergiu(self.negativas.next()):
                    break
         
         
    def __str__(self):
        return str((float(self.soma_parcial), self.total_de_parcelas, 
                self.sequencia_alternada_de_parcelas))
        
    def plotar(self):
        plot([self.limite-self.epsilon] * self.total_de_parcelas)
        plot([self.limite] * self.total_de_parcelas)
        plot([self.limite+self.epsilon] * self.total_de_parcelas)
        plot(self.soma_acumulada)
        plot(self.soma_acumulada, 'o')
            

def converge(L, e=0.1):
    c = Converge(L, e)
    c.converge()
    return c