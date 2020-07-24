#!/usr/bin/python
#coding: utf-8

#   Calculo Numerico (SME0602) - Projeto Pratico 1 
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia
#
#   Para rodar (no terminal linux): python main.py
#   Os resultados sao salvos no arquivo resultados.txt

import bisseccao
import secante
import newton
import halley
import ordem_convergencia as oc
import math

precisao_absoluta = 1e-16
f1_rcorreto = 0.739085133215  # raiz unica
f2_rcorreto = 3               # raiz unica
f3_rcorreto = 0               # infinitas raizes: (0, -1.2927, -4.7213, -7.8536 ...)

def main():
    # Salvar os resultados em um txt
    f = open("resultados", "w+")
    f.write("RESULTADO DE IMPLEMENTAÇÕES\n- Cálculo Numérico (SME0602) \n- Projeto Prático 1 \n- Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia \n\n")
    f.close()

    resultados_bisseccao( )
    resultados_secante( ) 
    resultados_newton( )
    resultados_halley( )


# x = 0.739085
def f1( x ):
    return x - math.cos(x)

# x = 3.0
def f2( x ):
    return x**3 - (9* x**2) + 27 * x - 27

# x = 0; x = -1.232695..; x = -7.85359...; ...
def f3( x ):
    return math.exp(x) - math.cos(x)


def resultados_bisseccao( ):
    f = open("resultados", "a")
    f.write("******** Bissecção ******** \n\n")
    f.close()

    resultados = []

    # Resultados do metodo da bisseccao
    resultados = bisseccao.bisseccao(f1, 0.0, math.pi, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f1_rcorreto)
    print_resultados(1, resultados, converg)

    resultados = bisseccao.bisseccao(f2, 0.0, 15.0, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f2_rcorreto)
    print_resultados(2, resultados, converg)

    resultados = bisseccao.bisseccao(f3, -0.5, 2.5, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f3_rcorreto)
    print_resultados(3, resultados, converg)

def resultados_secante( ):
    f = open("resultados", "a")
    f.write("\n******** Secante ********\n\n")
    f.close()

    resultados = []

    # Resultados do metodo da secante
    resultados = secante.secante(f1, 22.0, 6.0, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f1_rcorreto)
    print_resultados(1, resultados, converg)

    resultados = secante.secante(f2, 9.0, 11.0, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f2_rcorreto)
    print_resultados(2, resultados, converg)
    
    resultados = secante.secante(f3, 1.75, 2.15, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f3_rcorreto)
    print_resultados(3, resultados, converg)


def resultados_newton( ):
    f = open("resultados", "a")
    f.write("\n******** Newton ********\n\n")
    f.close()

    resultados = []

    # Resultados do metodo de newton
    resultados = newton.newton(f1, math.pi/2, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f1_rcorreto)
    print_resultados(1, resultados, converg)

    resultados = newton.newton(f2, 7.5, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f2_rcorreto)
    print_resultados(2, resultados, converg)

    resultados = newton.newton(f3, 1.0, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f3_rcorreto)
    print_resultados(3, resultados, converg)

    

def resultados_halley( ):
    f = open("resultados", "a")
    f.write("\n******** Halley ********\n\n")
    f.close()

    resultados = []

    # Resultados do metodo de halley
    resultados = halley.halley(f1, math.pi/2, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f1_rcorreto)
    print_resultados(1, resultados, converg)

    resultados = halley.halley(f2, 7.5, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f2_rcorreto)
    print_resultados(2, resultados, converg)

    resultados = halley.halley(f3, 1.0, precisao_absoluta)
    converg = oc.ordem_convergencia(resultados, f3_rcorreto)
    print_resultados(3, resultados, converg)

def print_resultados(index, resultados, converg):
    f = open("resultados", "a")
    f.write("Função " + str(index) + "\n")
    f.write(str(resultados) + "\n")
    f.write("Aprox. Inicial: " + str(resultados[0]) + "\n")
    f.write("Iterações: " + str(len(resultados)) + "\n") 
    f.write("Aprox. Final: " + str(resultados[len(resultados) - 1]) + "\n")
    f.write("Ordem de convergência: " + str(converg) + "\n\n")
    f.close()

if __name__ == "__main__":
    main()

