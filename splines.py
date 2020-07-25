# Baseado nos codigos vistos em aula
# Tem que instalar ums bibliotecas: 
    # python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
# Qual rapido uma spline cubica natural converge?
# Se a funcao for legal, converge melhor rs, se eu to interpolando uma funcao transcendental comum com com duas derivadas continuas e de se esperar que a ordem de convergencia seja proxima de 2, se nao tiver e de se esperar que seja menor que 2, ele fala umas coisas tipo funcao transcendental

import numpy as np
import sympy as sym
import matplotlib.pyplot as pp
import IPython.display as ipd
import scipy.interpolate as sci

def runge ( x ) :
  return 1.0 / ( 1.0 + 25.0 * (x ** 2) )

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

  '''
  # Vai ser plotado a funcao original e a interpolada
  pp.figure( figsize = ( 12, 8))
  x_plot = np.linspace(-12.0, 12.0, 1000)
  y_plot_aux = 1 / (1 + 25*x_plot*x_plot)

  pp.plot( x_plot, y_plot_aux)
  pp.plot( x_plot, cs(x_plot))
  pp.show()'''

  # Lista de erros maximos
  err = []
  n_points = []

  x_eval = np.linspace(-1.0, 1.0, 500)
  runge_x_eval = runge( x_eval )

  # Interpolar no mesmo intervalo a mesma funcao, mudando so o numero de pontos
  for n in range (7, 50) :
    # Definido os nos de acorfo com a funcao fornecida
    x_nodes = np.linspace(-1.0, 1.0, n)
    y_nodes = runge ( x_nodes )

    # Restricao natural
    cs = sci.CubicSpline(x_nodes, y_nodes, bc_type = ((2, 0.0), (2, 0.0)))

    # Calcular o erro atual
    cs_x_eval = cs( x_eval )
    curr_err = np.max( np.abs( cs_x_eval - runge_x_eval ) )
    err.append( curr_err )
    n_points.append( n )

  # Estimar o 'q' so para o par e so para o impar, pois o erro cai segundo aquele forma, ai eu estimei o 'q'(ordem de convergencia), tem que linearizar antes, aplicar log dos dois lados
  q_estimate( n_points[: : 2], err[: : 2] )
  q_estimate( n_points[1: : 2], err[1: : 2] )

  # Os pontos pares convergem melhor nesse caso, mas nao e uma diferenca muito expressiva
  # Ordem de convergencia proximo de 4 para par, e 3.xx para impar
  
  # Plotando o erro
  pp.figure( figsize = ( 12, 8))
  pp.plot (n_points, err)
  pp.show()

spline()