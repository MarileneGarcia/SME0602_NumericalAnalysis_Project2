# Baseado nos codigos apresentados em aula pelo professor
# Deve-se instalar algumas bibliotecas: 
    # python -m pip install --user numpy scipy matplotlib sympy 

# Escolher o valor de k
k = 100

# Escolhar as condicoes:
# Restricao natural (comente a linha 68)
cond = 'natural'
# Derivada conhecida nos extremos (remova o comentario da linha 68)
A = 2.5
B = 2.5

import numpy as np
import sympy as sym
import matplotlib.pyplot as pp
import scipy.interpolate as sci

def runge ( x ) :
  x_aux = []
  for j in  x :
    x_aux.append( 1.0 / ( 1.0 + 25.0 * (j*j) ))
  return x_aux

def q_estimate( n_points, err ):

  n_points = np.array( n_points, dtype='float' )
  err = np.array( err )
  y = np.log ( err )

  A = np.empty( (len( n_points ), 2) )
  A[ :, 0 ] = 1.0
  A[ :, 1 ] = np.log( n_points )
  AA = np.dot(A.T, A)

  b = np.dot( A.T, y )
  x = np.linalg.solve( AA, b )
  return -x[ 1 ]

def spline( ):

  # Listas de erros maximos e do numero de pontos
  err = []
  n_points = []
  
  # Definindo os valores da função runge nos pontos
  x_eval = []
  for i in range ( k ):
    x = -1 + ( 2*i )
    x_eval.append( x )
  runge_x_eval = runge( x_eval )

  # Interpolar no mesmo intervalo a funcao runge, alterando os pontos usados no spline
  for n in range (12, k - 1) :

    # Definido os nos de acordo com a funcao runge e quantidade de pontos
    x_nodes = []
    for i in range ( n ):
      x_n = -1 + ( 2*i )
      x_nodes.append(x_n)
    y_nodes = runge( x_nodes )

    # Aplicando o metodo spline interpolante usando a restricao natural
    cs = sci.CubicSpline(x_nodes, y_nodes, bc_type = ( cond ))

    # Aplicando o metodo spline interpolante usando a restricao da derivada conhecida nos extremos
    #cs = sci.CubicSpline(x_nodes, y_nodes, bc_type = ( (1, A), (1, B) ) )

    # Calcular o erro atual
    cs_x_eval = cs( x_eval )
    curr_err = np.max( np.abs( cs_x_eval - runge_x_eval ) )
    err.append( curr_err )
    n_points.append( n )

  q = q_estimate( n_points, err )
  print ( 'Valor da ordem de convergencia:',q )

  # Plotando o erro
  pp.plot (n_points, err)
  pp.savefig("erro2.png")

  pp.show()

spline()



