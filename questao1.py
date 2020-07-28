#   !/usr/bin/env python
#   coding: utf-8

#   Calculo Numerico (SME0602) - Projeto Pratico 2
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia
#
#   Para rodar (no terminal linux): python3 main.py

from matplotlib import pyplot as plt
import numpy as np

# Function to find the product term 
def proterm(i, value, x): 
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j]) 
    return pro

# Function for calculating divided difference table 
def dividedDiffTable(x, y, n): 
	for i in range(1, n): 
		for j in range(n - i): 
			y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j])) 
	return y

# Function for applying Newton's divided difference formula 
def applyFormula(value, x, y, n): 
	sum = y[0][0]

	for i in range(1, n): 
		sum = sum + (proterm(i, value, x) * y[0][i])
	
	return sum 

# Function for displaying divided difference table 
def printDiffTable(y, n): 
	for i in range(n): 
		for j in range(n - i): 
			print(round(y[i][j], 4), "\t", end = " ") 

		print("")

def y_x(x):
    return 1 / (1 + 25*x*x)

def main():
    # number of inputs given 
    k = 100
    x = [0 for i in range(k)]
    # y[][] is used for divided difference table where y[][0] is used for input 
    fx = [[0 for i in range(k)] for j in range(k)]

    for i in range(k):
        x[i] = -1 + 2*i/k
        fx[i][0] = y_x(x[i])

    # calculating divided difference table 
    fx=dividedDiffTable(x, fx, k)

    # displaying divided difference table 
    #print("*********** Tabela de Newton Dai ***********")
    #printDiffTable(fx, k)
    #print("\n")


    print("*********** Vetor de ek's ***********")
    pk = []
    ek = []
    x_max = -1
    e_max = 0
    for i in range(k):
        #print(i)
        x_aux = -1 + 2*i/k
        #print(y_x(x_aux))
        #print(applyFormula(x_aux, x, fx, k))
        ek.append(abs(y_x(x_aux)-applyFormula(x_aux, x, fx, k)))
        
        if ek[i] > e_max:
            x_max = x_aux
            e_max = ek[i]

    #print(ek)

    print("x_maximo: " + str(x_max))
    print("e_maximo: " + str(e_max))


    # ************** Plot grafico fx
    #fig = plt.figure(1)
    t = np.arange(-1, 1, 2/k)
    f_plot = y_x(t)
    fig1, ax = plt.subplots()
    ax.plot(t, f_plot, 'b')
    ax.grid()
    fig1.savefig("px.png")

    #fig = plt.figure(2)
    t2 = np.arange(0, k, 1)
    fig2, ax = plt.subplots()
    ax.set_yscale('log')
    ax.plot(t2, ek, 'r')
    fig2.savefig("erro.png")

    plt.show()

    plt.close(fig1)
    plt.close(fig2)

if __name__ == "__main__":
        main()
