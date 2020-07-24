#!/usr/bin/python
#coding: utf-8

#   Calculo Numerico (SME0602) - Projeto Pratico 2
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia
#
#   Para rodar (no terminal linux): python main.py

from __future__ import division
import math
import numpy as np

def main():
        k = 10
        fx = []
        fx = cria_funcao(k)
        print(fx)

def cria_funcao( k ):
        f = []
        for i in range(k):
                linha = []
                linha.append(float(-1 + 2*i/k))
                linha.append(float(1 / (1 + 25*pow(-1 + 2*i/k,2))))
                f.append(linha)

        return f
    

if __name__ == "__main__":
        main()

