#   !/usr/bin/python
#   coding: utf-8

#   Calculo Numerico (SME0602) - Projeto Pratico 2
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia
#
#   Para rodar (no terminal linux): python3 main.py


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

def func():
    

def main():
    # number of inputs given 
    k = 10
    x = [0 for i in range(k)]
    # y[][] is used for divided difference table where y[][0] is used for input 
    fx = [[0 for i in range(10)] for j in range(10)]

    for i in range(k):
        x[i] = -1 + 2*i/k
        fx[i][0] = 1 / (1 + 25*pow(x[i],2))

    # calculating divided difference table 
    fx=dividedDiffTable(x, fx, k)

    # displaying divided difference table 
    printDiffTable(fx, k)

    ek = [0 for i in range(k)]
    x_aux = 
    for i in range(k):
        for j in range(-1, 1, 0.1):
            fx_aux = 1 / (1 + 25*pow(x[i],2)

        ek[i] = abs()
    # value to be interpolated 
    value = -1

    # printing the value 
    print("\nValue at", value, "is", round(applyFormula(value, x, fx, k), 2)) 
    #print("\nValue a mao", value, "is", round(1 / (1 + 25*pow(value,2)), 2)) 

    # This code is contributed by mits 

if __name__ == "__main__":
        main()
